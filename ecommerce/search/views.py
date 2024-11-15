from django.shortcuts import render
from django.db.models import Q
from shop.models import Product

# Create your views here.
def search_products(request):
    if(request.method=="POST"):
        query=request.POST.get('q')  #reads the query value
        print(query)
        p=Product.objects.filter(Q(name__icontains=query) | Q(desc__icontains=query)) #filter the records matching with the query
        print(p)
        context={'pro':p,'query':query}

    return render(request,'search.html',context)


