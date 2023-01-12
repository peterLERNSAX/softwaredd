from django.urls import path

from . import views

urlpatterns = [
    path("",views.IndexView.as_view(),name="index-view"),
    path("create-user/",views.CreateUserView.as_view(),name="create-user-view"),
    path("login/",views.EmployeeLogin.as_view(),name="login-view"),
    path("list-employee/",views.ListEmployee.as_view(),name="list-employee-view"),
    path("delete-employee/<int:uid>",
        views.DeleteEmployee.as_view(),name="delete-employee-view"),
    

]