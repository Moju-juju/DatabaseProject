import requests
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Store, Customers, Orders, CartItems
from .forms import StoreForm, CustomerForm, OrderForm, CartItemsForm


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
    items = CartItems.objects.all()
    context = {'orders': orders, 'items': items}
    return render(request, "PmjoStore/orders.html", context)


def createOrder(request):
    form = OrderForm()
    form2 = CartItemsForm()
    if request.method == 'POST':
        if 'createOrder' in request.POST:
            form = OrderForm(request.POST)
            if form.is_valid():
                form.save()
        if 'addItems' in request.POST:
            form = CartItemsForm(request.POST)
            if form.is_valid():
                form.save()
        if 'submitForm' in request.POST:
            return redirect('/')

    context = {'form': form, 'form2': form2}
    return render(request, "PmjoStore/placeOrder_form.html", context)


def updateOrder(request, pk):
    orders = Orders.objects.filter(id=pk)
    items = CartItems.objects.filter(order_id_id=pk)

    context = {"orders": orders, "items": items}

    if request.method == 'POST':
        print(request.POST)
        if 'orders' in request.POST:
            order = Orders()
            order.cust_id = request.POST.get('add_order.cust_id')
            order.save()

    return render(request, "PmjoStore/order_form.html", context)


def deleteOrder(request, pk):
    order = Orders.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')
    context = {'object': order}
    return render(request, 'PmjoStore/delete_object.html', context)






































def updateOrderFake(request, pk):
    order = Orders.objects.get(id=pk)
    form = OrderForm(instance=order)

    if request.method == 'POST':
        form = OrderForm(request.POST, request.FILES, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, "PmjoStore/product_form.html", context)


def updateItemFake(request, pk):
    item = CartItems.objects.get(order_id_id=pk)
    form = OrderForm(instance=item)

    if request.method == 'POST':
        form = OrderForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, "PmjoStore/product_form.html", context)

