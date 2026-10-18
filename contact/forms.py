from .models import Contact

from django import forms


class ContactForm(forms.ModelForm):

    class Meta:

        model = Contact

        exclude = ["created_at" , "read_status"]


    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():

            field.label_suffix = " "

            field.widget.attrs.update({"class" : "form-control p-4" , "placeholder" : field_name.capitalize() if "_" not in field_name else field_name.replace("_", " ").title()})
