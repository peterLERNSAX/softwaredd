"""forms"""
from django import forms


class CreateEmployeeform(forms.Form):
    """EmployeeForm"""

    username = forms.CharField(label="Nutzername", max_length=200)
    password = forms.CharField(
        widget=forms.PasswordInput, max_length=64, min_length=4
    )
    check_password = forms.CharField(
        widget=forms.PasswordInput, max_length=64, min_length=4
    )
    usermanagement_field = forms.BooleanField(
        label="Nutzermanagemnt", required=False
    )
    layout_field = forms.BooleanField(label="Grundriss", required=False)
    database_field = forms.BooleanField(label="Datenbank", required=False)
    offer_field = forms.BooleanField(label="Angebot", required=False)
    offer_file_field = forms.BooleanField(
        label="Angebotsdatei", required=False
    )

    def is_valid(self) -> bool:
        password1 = self.data.get("password")
        password2 = self.data.get("check_password")
        print(password1)
        print(password2)
        if password1 != password2:
            print("abc")
            return False
        return super().is_valid()


class CreateCustomerForm(forms.Form):
    """CustomerForm"""

    firstname = forms.CharField(label="Vorname", max_length=200)
    sirname = forms.CharField(label="Nachname", max_length=200)
    email = forms.EmailField(label="Email")
    company_name = forms.CharField(
        label="Firmenname", required=False, max_length=200
    )


class CreateHardwareForm(forms.Form):
    """HArdware Form"""

    name = forms.CharField(label="Name", max_length=200)
    description = forms.CharField(
        label="Beschreibung", max_length=200, required=False
    )
    size = forms.CharField(label="Größe", max_length=200, required=False)
    weight = forms.FloatField(label="Gewicht", required=False)
    cable_length = forms.FloatField(label="Kabellänge", required=False)
    power_consumption = forms.FloatField(
        label="Stromverbrauch", required=False
    )
    workplace_ergonomics = forms.CharField(
        label="Arbeitsplatzergonomie", max_length=200, required=False
    )


class CreateOfferForm(forms.Form):
    """Offer Form"""

    customer = forms.IntegerField(required=False)
    offer_file = forms.IntegerField(required=False)
    layout = forms.IntegerField(required=False)
    description = forms.CharField(max_length=200, required=False)
