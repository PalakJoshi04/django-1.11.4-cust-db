from django.shortcuts import render
from .models import Customer
from .forms import CustomerForm


def index(request):
    return render(request, "index.html")


def people(request):
    form = CustomerForm()

    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            p = Customer()
            p.first_name = form.cleaned_data["first_name"]
            p.last_name = form.cleaned_data["last_name"]
            p.save()
        else:
            form = CustomerForm()

    po = Customer.objects.all()
    return render(request, "people.html", {"people": po, "form": form})
