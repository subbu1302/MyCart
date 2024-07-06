from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponse
from django.shortcuts import render, redirect

from Shop.models import Product, Customer
from Shop.models import Category

# Create your views here.
def home(request):

    categories=Category.objects.all()
    categoryID=request.GET.get('category')
    if categoryID:
        product=Product.get_category_id(categoryID)
    else:
        product = Product.objects.all()
    p={'product':product,'categories':categories}
    return render(request,'index.html',p)
#signUp Form
def signup(request):
    if request.method=='GET':
        return render(request,'signup.html')
    else:
        fn=request.POST['fn']
        ln=request.POST['ln']
        em=request.POST['em']
        ph=request.POST['ph']
        pa=request.POST['pa']
        pas=make_password(pa)
        u=[fn,ln,em,ph,pa]
        print(u)
        uservalues={
            'fn':fn,
            'ln':ln,
            'em':em,
            'ph':ph,
            'pa':pas
            }
        #storing object
        customerdata=Customer(First_Name=fn,Last_Name=ln,Email=em,Phone=ph,Password=pas)
        error_msg=None
        success=None
        if (not fn):
            error_msg='First Name Should Not be empty'
        elif (not ln):
            error_msg='Last Name Should Not be empty'
        elif (not em):
            error_msg='Email  Should Not be empty'
        elif (not ph):
            error_msg='Phone  Should Not be empty'
        elif (not pas):
            error_msg='Password  Should Not be empty'
        elif (customerdata.isexist()):
            error_msg='Email already exists'
        elif (customerdata.phoneexist()):
            error_msg = 'Phone already exists'
        elif (not error_msg):
            success='Account created successfully'
            customerdata.save()
            msgs={'success':success}
            return render(request,'signup.html', msgs)

        msgs={'error':error_msg,'success':success,'uservalues':uservalues}
        return render(request,'signup.html',msgs)

def login(request):
    if request.method=='GET':
        return render(request,'login.html')
    else:
        email=request.POST['email']
        password=request.POST['password']
        users=Customer.getemail(email)
        error=None
        if users:
            check=check_password(password,users.Password)
            if check:
                return redirect('/')
            else:
                error='password is incorrect'
                msg1={'errors':error}
                return render(request,'login.html',msg1)
        else:
            error = 'Email is incorrect'
            msg1 = {'errors': error}
            return render(request, 'login.html', msg1)
