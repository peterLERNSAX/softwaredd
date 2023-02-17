"""forms"""
from django import forms

class CreateEmployeeform(forms.Form):
    """EmployeeForm"""
    username = forms.CharField(label="Nutzername",max_length=200)
    password = forms.CharField(widget=forms.PasswordInput,max_length=64,min_length=4)
    check_password = forms.CharField(widget=forms.PasswordInput,max_length=64,min_length=4)
    usermanagement_field = forms.BooleanField(label="Nutzermanagemnt",required=False)
    layout_field = forms.BooleanField(label="Grundriss",required=False)
    database_field = forms.BooleanField(label="Datenbank",required=False)
    offer_field = forms.BooleanField(label="Angebot",required=False)
    offer_file_field = forms.BooleanField(label="Angebotsdatei",required=False)

    def is_valid(self) -> bool:
        password1 = self.data.get("password")
        password2 = self.data.get("check_password")
        if password1 != password2:
            return False
        return super().is_valid()