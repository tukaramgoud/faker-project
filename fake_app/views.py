from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse
from faker import Faker
# Create your views here.
fake = Faker()

def Fake_view(request):
    for i in range(10):
        fake_name=fake.name()
        fake_mobile=fake.random_int(min=12345,max=89045)
        fake_loc=fake.random_element(elements=('hyd','vixav','tirupathi'))

    data=person(
        name=fake_name,
        mobile=fake_mobile,
        loc=fake_loc,
    )
    data.save()

    return redirect('data')

def display_data(request):
    data=person.objects.all()
    return render(request,'display.html',{'data':data})
