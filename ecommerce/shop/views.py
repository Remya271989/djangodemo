from django.shortcuts import render,redirect
from shop.models import Category,Product
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def categories(request):
    c=Category.objects.all()
    context={'cat':c}
    return render(request,'categories.html',context)

def products(request,p):
    c=Category.objects.get(id=p)
    p=Product.objects.filter(category=c)
    context={'categories':c,'product':p}
    return render(request,'products.html',context)

def product_details(request,p):
    pro=Product.objects.get(id=p)
    context={'product':pro}
    return render(request,'details.html',context)


def register(request):
    if(request.method=='POST'):
        u=request.POST['u']
        p = request.POST['p']
        cp = request.POST['cp']
        f = request.POST['f']
        l = request.POST['l']
        e = request.POST['e']
        if(p==cp):
            u=User.objects.create_user(username=u,password=p,email=e,first_name=f,last_name=l)
            u.save()
            return redirect('shop:categories')
        else:
            return HttpResponse("Passwords are not same")

    return render(request,"register.html")

def user_login(request):
    if(request.method=='POST'):
        u=request.POST['u']
        p = request.POST['p']
        user=authenticate(username=u,password=p)
        if user:
            login(request,user)
            return redirect('shop:categories')
        else:
            return HttpResponse("Invalid Credentials")
    return render(request,"login.html")

@login_required
def user_logout(request):
    logout(request)
    return redirect('shop:login')

@login_required
def addcategories(request):
    if(request.method=="POST"):
        n=request.POST['n']
        i=request.FILES['i']
        d=request.POST['d']
        c=Category.objects.create(name=n,image=i,description=d)
        c.save()
        return redirect('shop:categories')

    return render(request,'addcategories.html')

@login_required
def addproducts(request):
    if (request.method == "POST"):
        n = request.POST['n']
        i = request.FILES['i']
        d = request.POST['d']
        s = request.POST['s']
        p = request.POST['p']
        c=request.POST['c']

        cat=Category.objects.get(name=c)

        p = Product.objects.create(name=n, image=i, desc=d,stock=s,price=p,category=cat)
        p.save()
        return redirect('shop:categories')

    return render(request,'addproducts.html')


@login_required
def addstock(request,p):
    product=Product.objects.get(id=p)
    if(request.method=="POST"):
        product.stock=request.POST['s']
        product.save()
        return redirect('shop:product_details',p)

    context={'pro':product}

    return render(request,'addstock.html',context)













