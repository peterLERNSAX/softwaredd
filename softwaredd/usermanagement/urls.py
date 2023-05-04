"""
urls
"""

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
    path(
        "geschaeftsprozess/",
        views.GeschaeftsprozessView.as_view(),
        name="geschaeftsprozess-view",
    ),
    path(
        "notwendigedaten/",
        views.NotwendigedatenView.as_view(),
        name="notwendigedaten-view",
    ),
    path("sequenz/", views.SequenzView.as_view(), name="sequenz-view"),
    path("use-case/", views.UseCaseView.as_view(), name="use-case-view"),
    path("copyright/", views.CopyrightView.as_view(), name="copyright-view"),
    path("webserver/", views.WebserverView.as_view(), name="webserver-view"),
    path(
        "grundrisse/", views.ListLayoutView.as_view(), name="list-layout-view"
    ),
    path(
        "angebotsdateien/",
        views.ListOfferView.as_view(),
        name="list-offer-view",
    ),
    path(
        "kunden/", views.ListCustomerView.as_view(), name="list-customer-view"
    ),
    path(
        "hardware/",
        views.ListHardwareView.as_view(),
        name="list-hardware-view",
    ),
    path("angebote/", views.ListOffersView.as_view(), name="list-offers-view"),
    path(
        "hardware/erstellen/",
        views.CreateHardwareView.as_view(),
        name="create-hardware-view",
    ),
    path(
        "kunden/erstellen/",
        views.CreateCustomerView.as_view(),
        name="create-customer-view",
    ),
    path(
        "angebot/erstellen/",
        views.CreateOfferView.as_view(),
        name="create-offer-view",
    ),
    path(
        "layout/erstellen/",
        views.CreateLayoutView.as_view(),
        name="create-layout-view",
    ),
    path(
        "kunden/löschen/<int:id>/",
        views.DeleteCustomerView.as_view(),
        name="delete-customer-view",
    ),
    path(
        "angebote/löschen/<int:id>/",
        views.DeleteOfferView.as_view(),
        name="delete-offer-view",
    ),
    path(
        "angebotsdateien/löschen/<int:id>/",
        views.DeleteOfferFileView.as_view(),
        name="delete-offer-file-view",
    ),
    path(
        "hardware/löschen/<int:id>/",
        views.DeleteHardwareView.as_view(),
        name="delete-hardware-view",
    ),
    path(
        "grundrisse/löschen/<int:id>/",
        views.DeleteLayoutView.as_view(),
        name="delete-layout-view",
    ),
]
