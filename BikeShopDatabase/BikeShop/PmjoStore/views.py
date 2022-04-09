from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Store
from .forms import StoreForm


# Create your views here (This is the logic that gets executed when the URLS are activated).
def products(request):
    msg = 'hello you are on the home page'
    stores = Store.objects.all()
    context = {'stores': stores}
    return render(request, 'PmjoStore/product.html', context)


def product(request, pk):
    productObj = None
    #for i in productsList:
     #   if i['id'] == pk:
      #      productObj = i
    return render(request, 'PmjoStore/single-product.html')


def createstore(request):
    form = StoreForm()

    if request.method == 'POST':
        form = StoreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, "PmjoStore/product_form.html", context)


def updateProject(request, pk):
    product = Store.objects.get(id=pk)
    form = StoreForm(instance=product)

    if request.method == 'POST':
        form = StoreForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, "Products/product_form.html", context)


def deleteProject(request, pk):
    product = Store.objects.get(id=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('/')
    context = {'object': product}
    return render(request, 'Products/delete_object.html', context)