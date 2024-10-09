from django import forms
from .models import UserModel, HouseModel


class UserForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ["name", "surname", "email"]

class HouseForm(forms.Form):
    class Meta:
        model = HouseModel
        fields = ["user", "description", "sq_meters", "private_bath"]
        help_texts = {
            'description': "Insert adress too in description"
        }