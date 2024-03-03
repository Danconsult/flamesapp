from django.shortcuts import render,redirect
from . logic import FlamesApp
from django.contrib import messages
from .forms import ContactForm
# Create your views here.

def index(request):
    return redirect("app")

def suggest(request):
    form =  ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Your form has been submitted successfully")
        else:
            form = ContactForm()
            messages.error(request,"Please fill the form properly")
    else:
        form = ContactForm()
    return render(request,'flamesapp/suggest.html', {'form':form})

def app(request):
    if request.method == "POST":
        your_name = (request.POST['your_name'])
        partner_name = (request.POST['partner_name'])
        if your_name.isalpha() and partner_name.isalpha():
            your_name = your_name.lower()
            partner_name = partner_name.lower()
            flameslogic = FlamesApp(your_name,partner_name)
            logic_out = flameslogic.app_logic()
            messages.success(request,logic_out)
        else:
            messages.error(request,"Please you are only allow to input name characters thanks.")

    return render(request,"flamesapp/index.html")

