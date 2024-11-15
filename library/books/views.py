from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    # context="Welcome to reading world"
    return render(request,"home.html")

from books.models import Book

@login_required
def view(request):
    k=Book.objects.all()
    context={'book':k}
    return render(request,"view.html",context)

@login_required
def add(request):
    if(request.method=="POST"):
        t=request.POST['t']
        a=request.POST['a']
        p=request.POST['p']
        pa=request.POST['pa']
        l=request.POST['l']

        i=request.FILES['i']
        f=request.FILES['f']

        b=Book.objects.create(title=t,author=a,price=p,pages=pa,language=l,cover=i,pdf=f)
        b.save()
        return view(request)

    return render(request,"add.html")

@login_required
def details(request,p):

    k=Book.objects.get(id=p)
    context={'book':k}
    return render(request,'details.html',context)


@login_required
def delete(request,p):
    k=Book.objects.get(id=p)
    k.delete()
    return redirect('books:View')

@login_required
def edit(request,p):
    k=Book.objects.get(id=p)
    if (request.method == "POST"):
        k.title = request.POST['t']
        k.author = request.POST['a']
        k.price = request.POST['p']
        k.pages = request.POST['pa']
        k.language = request.POST['l']
        if(request.FILES.get('i')==None):
            k.save()
        else:
            k.cover=request.FILES.get('i')

        if (request.FILES.get('f') == None):
            k.save()
        else:
            k.pdf = request.FILES.get('f')

        k.save()
        return redirect('books:View')

    context={'book':k}

    return render(request,'edit.html',context)
















