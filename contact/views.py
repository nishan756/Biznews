from django.shortcuts import render, redirect

from .models import ContactInfo

from .forms import ContactForm

from django.contrib import messages


def contact(request):

    form = ContactForm()

    contact_info = ContactInfo.objects.first()

    if request.method == "POST":

        form = ContactForm(data = request.POST)

        if form.is_valid():

            form.save()

            messages.success(request, "Thanks for contact with us. We'll notify your via email")

            return redirect("contact")

        messages.warning(request, form.errors)

    return render(request, "contact.html" , {"form" : form, "contact_info":contact_info})