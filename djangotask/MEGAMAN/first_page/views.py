from django.shortcuts import render
from django.http import HttpResponse
from .models import Car
# Create your views here.


dict_test = {"user":"lord" , "age":"99" , "URL":"QWEQWEQWE@@@@@@@@@@@@@@@@QWEQWE"}
listofusers = [{"name":"mohamed27", "age":27 },{"name":"mohamed26", "age":26 },{"name":"mohamed25", "age":25 },{"name":"mohamed24", "age":24 }
]
username = ["mohamed", "ahmed"]
dict = {"users" : listofusers}
def index(request):
    return render(request,'first_page/index.html', dict_test)
def dashboard(request):
    return render(request,'first_page/dashboard.html', dict)
def about(request):
    return render(request,'first_page/about.html', dict)
def product(request):
    return render(request,'first_page/product.html', {"products" :Car.objects.all()})
