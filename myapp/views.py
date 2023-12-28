from django.shortcuts import render,redirect,get_object_or_404
from .models import usermodel,House
def index(request):
    houses = House.objects.all()
    return render(request, 'index.html', {'houses': houses})

def signup(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        usermodel.objects.create(email=email,password=password)
        return redirect('login')
    return render(request,"signup.html")

def login(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        user=usermodel.objects.filter(email=email,password=password).first()
        if user:
            return render(request,"housedetails.html")
    return render(request,"login.html")

def housedetails(request):
    if request.method=='POST':
        owner_name = request.POST['owner_name']
        phone_number = request.POST['phone_number']
        cost_of_rent = request.POST['cost_of_rent']
        restrictions = request.POST['restrictions']
        bedrooms = request.POST['bedrooms']
        ac_non_ac = request.POST['ac_non_ac']
        myfile = request.FILES['photo']
        House.objects.create(
            owner_name=owner_name, 
            phone_number=phone_number, 
            cost_of_rent=cost_of_rent, 
            restrictions=restrictions, 
            bedrooms=bedrooms, 
            ac_non_ac=ac_non_ac, 
            photo=myfile
        )
        return redirect('index')
    return render(request,"housedetails.html")

def house_details(request, house_id):
    houses = get_object_or_404(House, pk=house_id)
    return render(request, 'house_details.html', {'houses': houses})
  
def user_rent(request):
    return render(request,"user_rent.html")
 
