"""views"""
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.views import LoginView
from django.http import HttpRequest
from django.shortcuts import HttpResponse, redirect, render
from django.views import View
from typing import Optional
import requests
from requests import Response
import json
from .forms import CreateEmployeeform
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
        return render(request,"usermanagement/list_layout.html",{"content":content_dict["response"]})


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
