from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from django.http import HttpRequest
from .forms import CreateEmployeeform
from.models import Employee
from django.contrib.auth.views import LoginView
from django.contrib.auth.hashers import make_password
# Create your views here.

class IndexView(View):
    """Indexview"""
    def get(self,request:HttpRequest)->HttpResponse:
        """get"""
        return render(request,"usermanagement/index.html")

class EmployeeLogin(LoginView):
    """Login"""
    template_name = "usermanagement/login.html"
    success_url = ""

class DeleteEmployee(View):
    """Delete Employee"""
    def post(self,request:HttpRequest,uid:int)->HttpResponse:
        """post"""
        employee = Employee.objects.get(pk = uid)
        employee.delete()
        return redirect("list-employee-view")
class ListEmployee(View):
    """List all Employees"""
    
    def get(self,request:HttpRequest)->HttpResponse:
        """get"""
        all_employee = Employee.objects.all()
        return render(request,"usermanagement/list_employee.html",{"employees":all_employee})

def employee_authentication(user:Employee,check_value:str)->bool:
    """check permissions of employee"""
    if check_value == "usermanagement":
        if not user.perm_usermanagement:
            return False
        return True

class CreateUserView(View):
    """Create user """
    def get(self,request:HttpRequest)->HttpResponse:
        """get"""
        #if not request.user.is_authenticated:
        #    return redirect("index-view")
        #if not type(request.user) is Employee:
        #    return redirect("index-view")
        #if not employee_authentication(request.user,"usermanagement"):
        #    return redirect("index-view")
        form = CreateEmployeeform()
        return render(request,"usermanagement/create_user.html",{"form":form})
    
    def post(self,request:HttpRequest)->HttpResponse:
        """post"""
        #if not request.user.is_authenticated:
        #    return redirect("index-view")
        #if not type(request.user) is Employee:
        #    return redirect("index-view")
        #if not employee_authentication(request.user,"usermanagement"):
        #    return redirect("index-view")
        form = CreateEmployeeform(data=request.POST)
        if not form.is_valid():
            return redirect("create-user-view")
        username = form.cleaned_data["username"]
        usermanagement = form.cleaned_data["usermanagement_field"]
        layout = form.cleaned_data["layout_field"]
        database = form.cleaned_data["database_field"]
        offer = form.cleaned_data["offer_field"]
        offer_file = form.cleaned_data["offer_file_field"]
        password = form.cleaned_data["password"]
        employee = Employee(username=username,password= make_password(password))
        employee.perm_usermanagement = usermanagement
        employee.perm_layout = layout
        employee.perm_database = database
        employee.perm_offer = offer
        employee.perm_offer_file = offer_file
        employee.save()
        return redirect("index-view")
