from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.models import auth
from .models import Food,FoodSharing
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.http import HttpResponse
from food.forms import CreateUserForm,LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.db.models import Q

@login_required(login_url='/signin/')
def home(request):
    if 'search' in request.GET:
        search=request.GET['search']
        data=Food.objects.filter(name__icontains=search)
    else:
        data=Food.objects.all()
    return render(request,'home.html',{'data':data})

def signup(request):
    form=CreateUserForm()

    if request.method=="POST":
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    context={'form':form}
    return render(request,'signup.html',context)


def signin(request):

    form=LoginForm()

    if request.method=="POST":
        form=LoginForm(request,data=request.POST)

        if form.is_valid():
            username=request.POST.get('username')
            password=request.POST.get('password')

            user=authenticate(request,username=username,password=password)

            if user is not None:
                auth.login(request,user)
                return redirect("home")
    context={'form':form}        

    return render(request,'signin.html',context)

def signout(request):
    auth.logout(request)
    return redirect("signin")

def changepassword(request):
    if request.method=="POST":
        form=PasswordChangeForm(user=request.user,data=request.POST)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            # messages.success(request,"Your password changed successfully")
            return redirect('signin')

    else:
        form=PasswordChangeForm(request.user)

    return render(request,'changepassword.html',{'form':form})

def about(request):
    return render(request,'about.html')
    

def contact(request):
    return render(request,'contact.html')

def profile(request):
    return render(request,'profile.html')

def foodsharing(request):
    return render(request,'sharingfood.html')

def foodsharingform(request):
    
    if request.method == "POST":
        fname=request.POST.get("fname")
        foodname=request.POST.get("foodname")
        mobile=request.POST.get("mobile")
        location=request.POST.get("location")
        quantity=request.POST.get("quantity")

        if request.POST.get("foodtype"):
            foodtype=request.POST.get("foodtype")

        data=FoodSharing.objects.create(
            fname=fname,
            foodname=foodname,
            mobile=mobile,
            location=location,
            quantity=quantity,
            foodtype=foodtype
            )    

        data.save()
        return render(request,'sharingfoodform.html')

    else:
        return render(request,'sharingfoodform.html')


    
def buycategory(request):
    return render(request,'buycategory.html')
    
def rawfood(request):
    if 'search' in request.GET:
        search=request.GET['search']
        data=FoodSharing.objects.filter(Q(foodtype__iexact='raw') & Q(foodname__icontains=search))
        if data:
            data=FoodSharing.objects.filter(foodname__icontains=search)
            return render(request,'rawfood.html',{'fooddetails':data})
        else:
            return HttpResponse('Data not found')
    else:
        food_details=FoodSharing.objects.all().filter(foodtype='raw')
        return render(request,'rawfood.html',{'fooddetails':food_details})


def cookedfood(request):
    food_details=FoodSharing.objects.all().filter(foodtype='cooked')
    return render(request,'cookedfood.html',{'fooddetails':food_details})

def packedfood(request):
    food_details=FoodSharing.objects.all().filter(foodtype='packed')
    return render(request,'packedfood.html',{'fooddetails':food_details})

# def buyingfood(request):
#     food_details=SharingFood.objects.all()
#     return render(request,'buyingfood.html',{'fooddetails':food_details})
