import requests
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import CreateView, DetailView

from .models import Store, Customers, Orders, CartItems, StockList, StoreEmployees, BikeProducts
from .forms import BrandForm, ProductsForm, StocksForm, StoreForm, CustomerForm, OrderForm, CartItemsForm
from django.db.models import F
from django.db.models import Q


# Create your views here (This is the logic that gets executed when the URLS are activated).
def stores(request):
    msg = 'hello you are on the home page'
    stores = Store.objects.all()
    context = {'stores': stores}
    return render(request, 'PmjoStore/store.html', context)


def store(request, pk):
    productObj = None
    #for i in productsList:
     #   if i['id'] == pk:
      #      productObj = i
    return render(request, 'PmjoStore/single-store.html')


def createstore(request):
    form = StoreForm()

    if request.method == 'POST':
        form = StoreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, "PmjoStore/store_form.html", context)


def updateStore(request, pk):
    store = Store.objects.get(id=pk)
    form = StoreForm(instance=store)

    if request.method == 'POST':
        form = StoreForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, "PmjoStore/store_form.html", context)


def deleteStore(request, pk):
    store = Store.objects.get(id=pk)
    if request.method == 'POST':
        store.delete()
        return redirect('/')
    context = {'object': store}
    return render(request, 'PmjoStore/delete_store.html', context)


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
    return render(request, "PmjoStore/customer_form.html", context)


def updateCustomer(request, pk):
    customer = Customers.objects.get(id=pk)
    form = CustomerForm(instance=customer)

    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, "PmjoStore/customers_form.html", context)


def deleteCustomer(request, pk):
    customer = Customers.objects.get(id=pk)
    if request.method == 'POST':
        customer.delete()
        return redirect('/')
    context = {'object': customer}
    return render(request, 'PmjoStore/delete_object.html', context)


def purchases(request, pk):
    customer = Customers.objects.get(id=pk)
    orders =  Orders.objects.filter(cust_id=customer)
    print(orders)
    items = CartItems.objects.all()
    context = {'customer': customer, 'orders:': orders, 'items': items}
    return render(request, 'PmjoStore/cust_purch.html', context)


def addBrand(request):
    form = BrandForm()

    if request.method == 'POST':
        form = BrandForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, "PmjoStore/brand_form.html", context)


def stockCtrl(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    print('SEARCH:', search_query)

    stores = Store.objects.filter(name__icontains=search_query)
    print(stores)
    storeID = Store.objects.filter(name=stores)
    #print(bikeID)

    stocks = StockList.objects.filter(store_id_id__in=stores).order_by('store_id')
    print([p for p in stocks])

    context = {'stocks': stocks, 'search_query': search_query}
    return render(request, 'PmjoStore/stock_ctrl_panel.html', context)


def addStock(request):
    form = StocksForm()

    if request.method == 'POST':
        form = StocksForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, "PmjoStore/stock_form.html", context)


def updateStock(request, pk):
    stock = StockList.objects.get(id=pk)
    form = StocksForm(instance=stock)

    if request.method == 'POST':
        form = StocksForm(request.POST, request.FILES, instance=stock)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, "PmjoStore/stock_form.html", context)


def addProduct(request):
    form = ProductsForm()

    if request.method == 'POST':
        form = ProductsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, "PmjoStore/product_form.html", context)


def orders(request):
    orders = Orders.objects.all()
    items = CartItems.objects.all()
    context = {'orders': orders, 'items': items}
    return render(request, "PmjoStore/orders.html", context)


def CreateOrder(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            return redirect('PmjoStore:update-order', pk=order.pk)
    else:
        form = OrderForm()
    context = {'form': form}
    return render(request, 'PmjoStore/new_order_form.html', context)


def add_item_to_order(request, pk):
    order = Orders.objects.get(id=pk)
    if request.method == 'POST':
        form = CartItemsForm(request.POST or None, initial={'order_id': order})

        if form.is_valid():
            form.save()

            return redirect('PmjoStore:update-order', pk=order.pk)
    else:
        form = CartItemsForm()
        stock_lists = StockList.objects.filter(store_id=order.store_staff_id.store_id)
        bike_prod_ids = []
        for stock_list in stock_lists:
            bike_prod_ids.append(stock_list.bike_prod_id.id)

        bike_products = BikeProducts.objects.filter(id__in=bike_prod_ids)
        form.fields['bike_prod_id'].queryset = bike_products
        #form.fields['order_id'].initial = order
    # if 'addItems' in request.POST:
    #     quantitySold = request.POST['quantity_sold']
    #     # stock_lists.quantity = F('quantity') - quantitySold
    #     # stock_lists.save()
    #     print("quantity sold", quantitySold)

    return render(request, 'PmjoStore/add_item.html', {'form': form})

# def createOrder(request):
#     form = OrderForm()
#     form2 = CartItemsForm()
#     if request.method == 'POST':
#         if 'createOrder' in request.POST:
#             form = OrderForm(request.POST)
#             if form.is_valid():
#                 form.save()
#         if 'addItems' in request.POST:
#             form = CartItemsForm(request.POST)
#             if form.is_valid():
#                 form.save()
#         if 'submitForm' in request.POST:
#             return redirect('/')
#
#     context = {'form': form, 'form2': form2}
#     return render(request, "PmjoStore/new_order_form.html", context)


#def createOrder(request):
    # form = OrderForm()
    # context = {'form': form}
    # if request.method == 'POST':
    #     form = OrderForm(request.POST or None)
    #     if form.is_valid():
    #         order = form.save()
    #         return redirect('order-details', pk=order.id)


            # orderNumber = request.POST['id']
            # print(orderNumber)
            # form.save()
                # store = request.POST['store_staff_id']
                # #currentOrder = Orders.objects.get(id=)
                # storestaff = StoreEmployees.objects.get(id=store)
                # print(storestaff.store_id)
                # #storeStock = StockList.objects.filter(store_id_id=storestaff.store_id, bike_prod_id_id= )
                # #print(storeStock)
                # print('store '+ store)
                # #employee = storestaff['staff_id']
                # print('store staff ' + str(storestaff))
                # #print('store staff ' + str(employee))
                # bikeChoices = StockList.objects.filter(store_id=storestaff.store_id)
                # print(bikeChoices)
                # context.update({'bikeChoices': bikeChoices})


    # return render(request, "PmjoStore/orderDetail.html/{{}}", context)

def addItems(request, pk):
    context = {'form': form, 'form2': form2}
    if 'addItems' in request.POST:
        form2 = CartItemsForm(request.POST)
        if form2.is_valid():
            form2.save()
            print(form2)
            # Get order ID
            order = request.POST['order_id']
            print('order' + order)
            # Match Order ID with Order
            # Get Order Number
            currentOrder = Orders.objects.get(id=order)
            print(currentOrder)
            # Match Order with Store Staff ID table
            stsf = currentOrder.store_staff_id.id
            print(stsf)
            # Match Store Staff ID with Store table to get the store
            store = StoreEmployees.objects.get(id=stsf)
            store = store.store_id

            print("store" + str(store))
            # Get the bike prod id from the order
            bike = request.POST['bike_prod_id']
            # Match Stocklist ID with Store ID
            stock = StockList.objects.get(store_id_id=store, bike_prod_id_id=bike)
            print("Stock" + str(stock))
            # Remove quantity from stocklist
            quantitySold = request.POST['quantity_sold']
            stock.quantity = F('quantity') - quantitySold
            stock.save()

            answer = request.POST['bike_prod_id']
            print('answer', answer)

            if stock.quantity == 0:
                stock.delete()
        else:
            print('not good')

            # stock.quantity = stock.quantity - quantity

    if 'submitForm' in request.POST:
        return redirect('/')
    return render(request, "PmjoStore/new_order_form.html", context)


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


def searchPage(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    print('SEARCH:', search_query)

    products = BikeProducts.objects.filter(name__icontains=search_query)
    print(products)
    bikeID = BikeProducts.objects.filter(name=products)
    #print(bikeID)

    stockItem = StockList.objects.filter(bike_prod_id_id__in=products).order_by('-bike_prod_id')#.values('store_id')
    print([p for p in stockItem])
    #print(stores.values('store_id').get()['store_id'])
    #storesX = StockList.objects.filter(bike_prod_id__=search_query).values('store_id')
    #print([p for p in storesX])

    #storesInfo = Store.objects.filter(id=stores)

    #print([p for p in storesInfo])
    #print(storesInfo)

    context = {'stockItems': stockItem, 'search_query': search_query}
    return render(request, 'PmjoStore/lookup.html', context)


def pieChart(request):
    labels = []
    data = []

    queryset = Store.objects.all()
    orders = Orders.objects.all()
    for store in queryset:
        labels.append(store.name)
        sales = Orders.objects.filter(store_staff_id_store_id_id = queryset).count()
        data.append(sales)

    return render(request, 'PmjoStore/pie_chart.html', {
        'labels': labels,
        'data':data,
    })










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