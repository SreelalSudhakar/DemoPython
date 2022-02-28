from django.shortcuts import render
from shop.models import Product
# Create your views here.


def SearchResult(request):
    query = None
    products = None
    if request.method == 'POST':
        query = request.POST['searched']
        products = Product.objects.all().filter(name__contains=query)
    # if 'q' in request.GET:
    #     query = request.GET('searched')
    #     products = Product.objects.filter(Q(name__contains=query))
    return render(request,"search.html",{'query1':query,'products':products})    