from django.shortcuts import render , redirect
from django.http import HttpResponse

from .forms import carForm
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



def singleCar (request,id):
    singleCar= Car.objects.get(pk = id)
    return render(request,'first_page/viewcar.html',{"car":singleCar})

def createCar(request):
    Car = carForm(request.POST, request.FILES)
    if Car.is_valid():
        Car.save() 
    else :
        print("not valid")
        return render(request,'first_page/createcar.html',{"form":carForm})
    return redirect('product') 
    

def editCar (request,id):
    carID = Car.objects.get(pk = id)
    form = carForm(request.POST or None,instance=carID)
    if form.is_valid():
        form.save()
    else :
        print("not valid")
        return render(request,'first_page/carupdate.html',{"car" : carID,"form":form})
    return redirect('product') 

def deleteCar (request,id):
    car = Car.objects.get(pk = id)
    car.delete()
    cars = Car.objects.all().order_by('id')
    return redirect('product') 