from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Store, Customers, Orders
from .forms import StoreForm, CustomerForm


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
    return render(request, "PmjoStore/product_form.html", context)


def deleteProject(request, pk):
    product = Store.objects.get(id=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('/')
    context = {'object': product}
    return render(request, 'PmjoStore/delete_object.html', context)


def customers(request):
    customers = Customers.objects.all()
    context = {'customers': customers}
    return render(request, "PmjoStore/customers.html", context)


def createCustomer(request):
    form = CustomerForm()

    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, "PmjoStore/product_form.html", context)


def updateCustomer(request, pk):
    customer = Customers.objects.get(id=pk)
    form = CustomerForm(instance=customer)

    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, "PmjoStore/product_form.html", context)


def deleteCustomer(request, pk):
    customer = Customers.objects.get(id=pk)
    if request.method == 'POST':
        customer.delete()
        return redirect('/')
    context = {'object': customer}
    return render(request, 'PmjoStore/delete_object.html', context)


def orders(request):
    orders = Orders.objects.all()
    context = {'orders': orders}
    return render(request, "PmjoStore/orders.html", context)

