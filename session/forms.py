from django import forms 

from django.contrib.auth import get_user_model

from django.core.exceptions import ValidationError

User = get_user_model()


class UserSignUpForm(forms.ModelForm):

    confirm_password = forms.CharField(widget = forms.PasswordInput(attrs = {"placeholder":"Confirm Password"}))

    class Meta:

        model = User

        exclude = ["is_active" , "is_staff" , "joined_at" , "is_superuser" , "groups" , "user_permissions", "user_type"]


    def __init__(self, *args, **kwargs):
        
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():

            field.widget.attrs.update({"class" : "form-control","placeholder":field_name.capitalize() if "_" not in field_name else field_name.replace("_" , " ").title()})

    def clean(self):
        
        cleaned_data = super().clean()

        password = cleaned_data.get("password")

        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:


            self.add_error("password" , "Password didn't matched.")

            self.add_error("confirm_password" , "Password didn't matched.")

        return cleaned_data

class PasswordChangeForm(forms.Form):

    old_password = forms.CharField(

        widget = forms.PasswordInput(
            attrs = {
                "type":"password",
                "class":"form-control",
                "placeholder":"Enter Old Password",
                "required":True
            }
        )
    )

    new_password = forms.CharField(
    
        widget = forms.PasswordInput(
            attrs = {
                "type":"password",
                "class":"form-control",
                "placeholder":"Enter New Password",
                "required":True

            }
        )
    )

    confirm_password = forms.CharField(
    
        widget = forms.PasswordInput(
            attrs = {
                "type":"password",
                "class":"form-control",
                "placeholder":"Retype New Password",
                "required":True

            }
        )
    )

    def clean(self):

        cleaned_data = super().clean()

        old_password = cleaned_data.get("old_password")

        new_password = cleaned_data.get("new_password")

        confirm_password = cleaned_data.get("confirm_password")

        if old_password == new_password:

            self.add_error("new_password", "New password can't same as old password")

        if new_password != confirm_password:

            self.add_error("confirm_password", "Please confirm your new password")

        return cleaned_data