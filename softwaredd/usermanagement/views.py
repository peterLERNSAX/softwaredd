"""views"""
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.views import LoginView
from django.http import HttpRequest
from django.shortcuts import HttpResponse, redirect, render
from django.views import View
from typing import Optional, Any
import requests
from requests import Response
import json
from .forms import CreateEmployeeform, CreateCustomerForm, CreateHardwareForm, CreateOfferForm
from .models import Employee

API_URL = "http://127.0.0.1:8000"

# Create your views here.


def get_employee(request: HttpRequest) -> Optional[Employee]:
    """gets an employee"""
    if request.user.is_authenticated:
        employ: Employee = Employee.objects.get(username=request.user.username)
        return employ
    return None


class IndexView(View):
    """Indexview"""

    def get(self, request: HttpRequest) -> HttpResponse:
        """get"""
        employ = get_employee(request)
        return render(request, "usermanagement/index.html", {"employ": employ})


class DocsView(View):
    """Docs"""

    def get(self, request: HttpRequest) -> HttpResponse:
        """get"""
        employ = get_employee(request)
        return render(
            request, "usermanagement/index_webserver.html", {"employ": employ}
        )


class GeschaeftsprozessView(View):
    """Geschäftsprozesse"""

    def get(self, request: HttpRequest) -> HttpResponse:
        """get"""
        employ = get_employee(request)
        return render(
            request,
            "usermanagement/geschaeftsprozess.html",
            {"employ": employ},
        )


class NotwendigedatenView(View):
    """Notwendigedaten"""

    def get(self, request: HttpRequest) -> HttpResponse:
        """get"""
        employ = get_employee(request)
        return render(
            request, "usermanagement/notwendigedaten.html", {"employ": employ}
        )


class SequenzView(View):
    """Sequenz"""

    def get(self, request: HttpRequest) -> HttpResponse:
        """get"""
        employ = get_employee(request)
        return render(
            request, "usermanagement/sequenz.html", {"employ": employ}
        )


class UseCaseView(View):
    """Use-Case"""

    def get(self, request: HttpRequest) -> HttpResponse:
        """get"""
        employ = get_employee(request)
        return render(
            request, "usermanagement/use-case.html", {"employ": employ}
        )


class CopyrightView(View):
    """Copyright"""

    def get(self, request: HttpRequest) -> HttpResponse:
        """get"""
        employ = get_employee(request)
        return render(
            request, "usermanagement/copyright.html", {"employ": employ}
        )


class WebserverView(View):
    """Webserver"""

    def get(self, request: HttpRequest) -> HttpResponse:
        """get"""
        employ = get_employee(request)
        return render(
            request, "usermanagement/webserver.html", {"employ": employ}
        )


# pylint: disable=too-many-ancestors
class EmployeeLogin(LoginView):
    """Login"""

    template_name = "usermanagement/login.html"
    success_url = "{% url 'index-view'%}"

    def form_invalid(self, form) -> HttpResponse:
        messages.warning(self.request,"Benutzerdaten nicht richtig!")
        return super().form_invalid(form)


class LogoutView(View):
    """Logout"""

    def get(self, request: HttpRequest) -> HttpResponse:
        """get"""
        logout(request)
        messages.info(request, "Erfolgreich abgemeldet")
        return redirect("index-view")


class DeleteEmployee(View):
    """Delete Employee"""

    def post(self, request: HttpRequest, uid: int) -> HttpResponse:
        """post"""
        if not request.user.is_authenticated:
            messages.error(request, "Unzureichende Berechtigungen")
            return redirect("index-view")
        employee = Employee.objects.get(pk=uid)
        employee.delete()
        messages.success(request, "Nutzer erfolgreich gelöscht")
        return redirect("list-employee-view")


class ListEmployee(View):
    """List all Employees"""

    def get(self, request: HttpRequest) -> HttpResponse:
        """get"""
        all_employee = Employee.objects.all()
        employ = get_employee(request)
        return render(
            request,
            "usermanagement/list_employee.html",
            {"employees": all_employee, "employ": employ},
        )


def employee_authentication(user: Employee, check_value: str) -> bool:
    """check permissions of employee"""
    check_user: Employee = Employee.objects.get(username=user.username)
    if check_value == "usermanagement":
        if not check_user.perm_usermanagement:
            return False
        return True
class ListLayoutView(View):
    """View for listing layouts"""

    def get(self,request:HttpRequest)->HttpResponse:
        """get"""
        url = API_URL+"/dbApi/v1/post/layout/all/"
        employee:Employee = Employee.objects.get(pk=request.user.pk)
        content:Response=requests.post(url,json=employee.get_permission_dict())
        content_dict = (json.loads(content.content))
        employ = get_employee(request)
        return render(request,"usermanagement/list_layout.html",{"content":content_dict["response"],"employ":employ})

class ListCustomerView(View):
    """View for listing customers"""

    def get(self,request:HttpRequest)->HttpResponse:
        """get"""
        if not request.user.is_authenticated:
            messages.warning(request,"Nicht Authentifiziert!")
            return redirect("index-view")
        url = API_URL+"/dbApi/v1/post/customer/all/"
        employee:Employee = Employee.objects.get(pk=request.user.pk)
        content:Response=requests.post(url,json=employee.get_permission_dict())
        content_dict = (json.loads(content.content))
        employ = get_employee(request)
        return render(request,"usermanagement/list_customer.html",{"content":content_dict["response"],"employ":employ})

class ListHardwareView(View):
    """View for listing hardware"""
    def get(self,request:HttpRequest)->HttpResponse:
        """get"""
        if not request.user.is_authenticated:
            messages.warning(request,"Nicht Authentifiziert!")
            return redirect("index-view")
        url = API_URL+"/dbApi/v1/post/hardware/all/"
        employee:Employee = Employee.objects.get(pk=request.user.pk)
        content:Response=requests.post(url,json=employee.get_permission_dict())
        content_dict = (json.loads(content.content))
        employ = get_employee(request)
        return render(request,"usermanagement/list_hardware.html",{"content":content_dict["response"],"employ":employ})

class CreateOfferView(View):
    """View for creating an offer"""

    def get(self,request:HttpRequest)->HttpResponse:
        """get"""
        if not request.user.is_authenticated:
            messages.warning(request,"Nicht Authentifiziert!")
            return redirect("index-view")
        employee:Employee = Employee.objects.get(pk=request.user.pk)
        if not employee.perm_offer:
            messages.warning(request,"Unzureichende Berechtigungen")
            return redirect("index-view")
        url_customer = API_URL+"/dbApi/v1/post/customer/all/"
        employee:Employee = Employee.objects.get(pk=request.user.pk)
        customers:Response=requests.post(url_customer,json=employee.get_permission_dict())
        customer_dict = (json.loads(customers.content))

        url_layout = API_URL+"/dbApi/v1/post/layout/all/"
        layouts:Response=requests.post(url_layout,json=employee.get_permission_dict())
        layout_dict = (json.loads(layouts.content))

        url_offer_files = API_URL+"/dbApi/v1/post/offer/file/all/"
        offer_files:Response=requests.post(url_offer_files,json=employee.get_permission_dict())
        offer_files_dict = (json.loads(offer_files.content))
        form = CreateOfferForm()
        employ = get_employee(request)
        return render(request,"usermanagement/create_offer.html",{"form":form,"employ":employ,"customers":customer_dict["response"],"layouts":layout_dict["response"],"offer_files":offer_files_dict["response"]})

    def post(self,request:HttpRequest)->HttpResponse:
        """post"""
        if not request.user.is_authenticated:
            messages.warning(request,"Nicht Authentifiziert!")
            return redirect("index-view")
        employee:Employee = Employee.objects.get(pk=request.user.pk)
        if not employee.perm_offer:
            messages.warning(request,"Unzureichende Berechtigungen")
            return redirect("index-view")
        form = CreateOfferForm(data=request.POST)
        customer = form.data["customer"]
        offer_file = form.data["offer_file"]
        layout = form.data["layout"]
        description = form.data["description"]
        data = {"customer":customer,"offer_file":offer_file,"layout":layout,"description":description}
        if customer == "":
            data.pop("customer")
        if offer_file =="":
            data.pop("offer_file")
        if layout =="":
            data.pop("layout")
        if description =="":
            data.pop("description")
        url = API_URL+"/dbApi/v1/post/offer/new/"
        content:Response=requests.post(url,json=employee.get_permission_dict(),params=data)
        assert(content,Response)
        if not content.status_code == 200:
            messages.warning(request,"Keine Verbindung zur Datenbank möglich")
            return redirect("create-offer-view")
        return redirect("list-offer-view")
        
class CreateCustomerView(View):
    """View for creating customers"""
    def get(self,request:HttpRequest)->HttpResponse:
        """get"""
        if not request.user.is_authenticated:
            messages.warning(request,"Nicht Authentifiziert!")
            return redirect("index-view")
        employee:Employee = Employee.objects.get(pk=request.user.pk)
        if not employee.perm_database:
            messages.warning(request,"Unzureichende Berechtigungen")
            return redirect("index-view")
        form = CreateCustomerForm()
        employ = get_employee(request)
        return render(request,"usermanagement/create_customer.html",{"form":form,"employ":employ})
    
    def post(self,request:HttpRequest)->HttpResponse:
        """post"""
        if not request.user.is_authenticated:
            messages.warning(request,"Nicht Authentifiziert!")
            return redirect("index-view")
        employee:Employee = Employee.objects.get(pk=request.user.pk)
        if not employee.perm_database:
            messages.warning(request,"Unzureichende Berechtigungen")
            return redirect("index-view")
        form = CreateCustomerForm(data=request.POST)
        firstname = form.data["firstname"]
        sirname = form.data["sirname"]
        email = form.data["email"]
        company_name = form.data["company_name"]
        data = {"firstname":firstname,"sirname":sirname,"email":email,"company_name":company_name}
        if company_name == "":
            data.pop("company_name")
        url = API_URL+"/dbApi/v1/post/customer/new/"
        content:Response=requests.post(url,json=employee.get_permission_dict(),params=data)
        assert(content,Response)
        if not content.status_code == 200:
            messages.warning(request,"Keine Verbindung zur Datenbank möglich")
            return redirect("create-customer-view")
        return redirect("list-customer-view")

class CreateHardwareView(View):
    """View for creating Hardware"""
    def get(self,request:HttpRequest)->HttpResponse:
        """get"""
        if not request.user.is_authenticated:
            messages.warning(request,"Nicht Authentifiziert!")
            return redirect("index-view")
        employee:Employee = Employee.objects.get(pk=request.user.pk)
        if not employee.perm_database:
            messages.warning(request,"Unzureichende Berechtigungen")
            return redirect("index-view")
        form = CreateHardwareForm()
        employ = get_employee(request)
        return render(request,"usermanagement/create_hardware.html",{"form":form,"employ":employ})
    
    def post(self,request:HttpRequest)->HttpResponse:
        """post"""
        if not request.user.is_authenticated:
            messages.warning(request,"Nicht Authentifiziert!")
            return redirect("index-view")
        employee:Employee = Employee.objects.get(pk=request.user.pk)
        if not employee.perm_database:
            messages.warning(request,"Unzureichende Berechtigungen")
            return redirect("index-view")
        form = CreateHardwareForm(data=request.POST)
        name:str = form.data["name"]
        description:Optional[str] = form.data["description"]
        size:Optional[str] = form.data["size"]
        weight:Optional[float] = form.data["weight"]
        cable_length:Optional[float] = form.data["cable_length"]
        power_consumption:Optional[float]=form.data["power_consumption"]
        workplace_ergonomics:Optional[str]=form.data["workplace_ergonomics"]
        data = {"name":name,"description":description,"size":size,
                "weight":weight,"cable_length":cable_length,"power_consumption":power_consumption,
                "workplace_ergonomics":workplace_ergonomics}
        if description == "":
            data.pop("description")
        if size == "":
            data.pop("size")
        if weight == "":
            data.pop("weight")
        if cable_length == "":
            data.pop("cable_length")
        if power_consumption == "":
            data.pop("power_consumption")
        if workplace_ergonomics == "":
            data.pop("workplace_ergonomics")
        url = API_URL+"/dbApi/v1/post/hardware/new/"
        content:Response=requests.post(url,json=employee.get_permission_dict(),params=data)
        assert(content,Response)
        if not content.status_code == 200:
            messages.warning(request,"Keine Verbindung zur Datenbank möglich")
            return redirect("create-hardware-view")
        return redirect("list-hardware-view")

class ListOffersView(View):
    """View for listing offers"""
    def get(self,request:HttpRequest)->HttpResponse:
        """get"""
        if not request.user.is_authenticated:
            messages.warning(request,"Nicht Authentifiziert!")
            return redirect("index-view")
        url = API_URL+"/dbApi/v1/post/offer/all/"
        employee:Employee = Employee.objects.get(pk=request.user.pk)
        content:Response=requests.post(url,json=employee.get_permission_dict())
        content_dict = (json.loads(content.content))
        url_customer = API_URL+"/dbApi/v1/post/customer/all/"
        employee:Employee = Employee.objects.get(pk=request.user.pk)
        customers:Response=requests.post(url_customer,json=employee.get_permission_dict())
        customer_dict = (json.loads(customers.content))

        url_layout = API_URL+"/dbApi/v1/post/layout/all/"
        layouts:Response=requests.post(url_layout,json=employee.get_permission_dict())
        layout_dict = (json.loads(layouts.content))

        url_offer_files = API_URL+"/dbApi/v1/post/offer/file/all/"
        offer_files:Response=requests.post(url_offer_files,json=employee.get_permission_dict())
        offer_files_dict = (json.loads(offer_files.content))
        employ = get_employee(request)
        return render(request,"usermanagement/list_offers.html",{"content":content_dict["response"],"employ":employ,"customers":customer_dict["response"],"layouts":layout_dict["response"],"offer_files":offer_files_dict["response"]})


class ListOfferView(View):
    """View for listing offer files"""

    def get(self,request:HttpRequest)->HttpResponse:
        """get"""
        url = API_URL+"/dbApi/v1/post/offer/file/all/"
        employee:Employee = Employee.objects.get(pk=request.user.pk)
        content:Response=requests.post(url,json=employee.get_permission_dict())
        content_dict = (json.loads(content.content))
        employ = get_employee(request)
        return render(request,"usermanagement/list_offer.html",{"content":content_dict["response"],"employ":employ})


class CreateUserView(View):
    """Create user"""

    def get(self, request: HttpRequest) -> HttpResponse:
        """get"""
        if not request.user.is_authenticated:
            messages.error(request, "Unzureichende Berechtigungen")
            return redirect("index-view")
        if not employee_authentication(request.user, "usermanagement"):
            messages.error(request, "Unzureichende Berechtigungen")
            return redirect("index-view")
        form = CreateEmployeeform()
        employ = get_employee(request)
        return render(
            request,
            "usermanagement/create_user.html",
            {"form": form, "employ": employ},
        )

    def post(self, request: HttpRequest) -> HttpResponse:
        """post"""
        if not request.user.is_authenticated:
            messages.error(request, "Unzureichende Berechtigungen")
            return redirect("index-view")
        if not employee_authentication(request.user, "usermanagement"):
            messages.error(request, "Unzureichende Berechtigungen")
            return redirect("index-view")
        form = CreateEmployeeform(data=request.POST)
        if not form.is_valid():
            messages.info(request, "Überprüfe die eingegebenen Daten und beachte, dass die Passwörter identisch sein müssen!")
            #time.sleep(5) sicher das wir das haben wollen? Es wird erst gesleept weil die message erst beim render nagezigt wird
            return redirect("create-user-view")
        username = form.cleaned_data["username"]
        usermanagement = form.cleaned_data["usermanagement_field"]
        layout = form.cleaned_data["layout_field"]
        database = form.cleaned_data["database_field"]
        offer = form.cleaned_data["offer_field"]
        offer_file = form.cleaned_data["offer_file_field"]
        password = make_password(form.cleaned_data["password"])
        try:
            Employee.objects.get(username=username)
            messages.warning(request, "Nutzer existiert bereits")
            return redirect("create-user-view")
        except Exception:
            employee = Employee(
                username=username, password=password
            )
            employee.perm_usermanagement = usermanagement
            employee.perm_layout = layout
            employee.perm_database = database
            employee.perm_offer = offer
            employee.perm_offer_file = offer_file
            employee.save()
            messages.success(request, "Nutzer erfolgreich erstellt")
            return redirect("index-view")
