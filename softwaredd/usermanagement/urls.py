from django.urls import path

from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index-view"),
    path(
        "create-user/", views.CreateUserView.as_view(), name="create-user-view"
    ),
    path("login/", views.EmployeeLogin.as_view(), name="login-view"),
    path(
        "list-employee/",
        views.ListEmployee.as_view(),
        name="list-employee-view",
    ),
    path(
        "delete-employee/<int:uid>",
        views.DeleteEmployee.as_view(),
        name="delete-employee-view",
    ),
    path("logout/", views.LogoutView.as_view(), name="logout-view"),
    path("docs/", views.DocsView.as_view(), name="show-webserver-view"),
    path("geschaeftsprozess/", views.GeschaeftsprozessView.as_view(), name="geschaeftsprozess-view"),
    path("notwendigedaten/", views.NotwendigedatenView.as_view(), name="notwendigedaten-view"),
    path("sequenz/", views.SequenzView.as_view(), name="sequenz-view"),
    path("use-case/", views.UseCaseView.as_view(), name="use-case-view"),
    path("copyright/", views.CopyrightView.as_view(), name="copyright-view"),
    path("webserver/", views.WebserverView.as_view(), name="webserver-view"),
]
