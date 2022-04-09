import datetime
import uuid

from django.db import models
from phone_field import PhoneField
from localflavor.us.us_states import STATE_CHOICES
from localflavor.us.models import USStateField


YEAR_CHOICES = [(r,r)for r in range(2000, datetime.date.today().year+1)]
BIKE_CATIES = (
    ('mountain_bike', 'Mountain Bike'),
    ('road_bike', 'Road Bike'),
    ('touring_bike', 'Touring Bike'),
    ('folding_bike', 'Folding Bike'),
    ('track_bike', 'Track Bike'),
    ('cruiser', 'Cruiser'),
    ('bmx', 'BMX'),
    ('recumbent', 'Recumbent'),
    ('utility', 'Utility'),
    ('trike', 'Trike'),
)

BIKE_BRANDS = (
    ('giant_bikes', 'Giant Bikes'),
    ('trek_bikes', 'Trek Bikes'),
    ('specialized', 'Specialized'),
    ('santa_cruz', 'Santa Cruz'),
    ('gt', 'GT'),
    ('yeti', 'Yeti'),
    ('cannondale', 'Cannondale'),
    ('marin', 'Marin'),
    ('diamondback', 'DiamondBack'),
)


# Create your models here (These are our database tables).
class Base(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    class Meta:
        abstract = True


class ZipCode(Base):
    zipCode = models.CharField(max_length=5, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = USStateField(choices=STATE_CHOICES, default='PA')

    def __str__(self):
        return self.zipCode


class Staff(Base):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = PhoneField(blank=True, help_text='Contact phone number')
    email = models.EmailField(max_length=100, blank=True)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    class Meta:
        verbose_name_plural = 'Staff'


class Store(Base):
    name = models.CharField(max_length=100, blank=True)
    phone = PhoneField(blank=True, help_text='Contact phone number')
    email = models.EmailField(max_length=100, blank=True)
    street = models.CharField(max_length=100, blank=True)
    #city = models.CharField(max_length=100, blank=True)
    #state = USStateField(choices=STATE_CHOICES, default='PA')
    #zipCode = models.CharField(max_length=5, blank=True)
    zipCode_id = models.OneToOneField(ZipCode, on_delete=models.CASCADE, blank=True, default=1)
    manager_id = models.OneToOneField(Staff, on_delete=models.CASCADE, blank=True, default=1)

    def __str__(self):
        return self.name


#class Managers(Base):
    #store_id = models.OneToOneField(Store, on_delete=models.CASCADE, blank=True, default=1)
    #staff_id = models.OneToOneField(Staff, on_delete=models.CASCADE, blank=True, default=1)

    #def __str__(self):
     #   return '{} {}'.format(self.staff_id.first_name, self.staff_id.last_name)

    #class Meta:
    #    verbose_name_plural = 'Managers'


class StoreEmployees(Base):
    staff_id = models.OneToOneField(Staff, on_delete=models.CASCADE, blank=True, default=1)
    #store_id = models.ForeignKey(Store, on_delete=models.CASCADE, blank=True, default=1)

    def __str__(self):
        return '{} {} - {}'.format(self.staff_id.first_name, self.staff_id.last_name, self.store_id)

    class Meta:
        verbose_name_plural = 'Products Employees'


class Customers(Base):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = PhoneField(blank=True, help_text='Contact phone number')
    email = models.EmailField(max_length=100, blank=True)
    street = models.CharField(max_length=100, blank=True)
    #city = models.CharField(max_length=100, blank=True)
    #state = USStateField(choices=STATE_CHOICES, default='PA')
    zipCode_id = models.OneToOneField(ZipCode, on_delete=models.CASCADE, blank=True, default=1)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    class Meta:
        verbose_name_plural = 'Customers'


class BikeCategory(Base):
    category = models.CharField(max_length=100, choices=BIKE_CATIES, unique=True)

    def __str__(self):
        return dict(BIKE_CATIES).get(self.category)

    class Meta:
        verbose_name_plural = 'Bike Categories'


class BikeBrands(Base):
    brand = models.CharField(max_length=100, choices=BIKE_BRANDS, unique=True)

    def __str__(self):
        return dict(BIKE_BRANDS).get(self.brand)

    class Meta:
        verbose_name_plural = 'Bike Brands'


class BikeProducts(Base):
    name = models.CharField(max_length=100)
    bike_cat_id = models.ForeignKey(BikeCategory, on_delete=models.CASCADE, blank=True, default=1)
    bike_brand_id = models.ForeignKey(BikeBrands, on_delete=models.CASCADE, blank=True, default=1)
    model_year = models.IntegerField(choices=YEAR_CHOICES, default=datetime.date.today().year)
    price = models.PositiveIntegerField(default=0)

    def __str__(self):
        return '{} {} {}'.format(self.model_year, dict(BIKE_BRANDS).get(self.bike_brand_id.brand),
                              self.name)

    class Meta:
        verbose_name_plural = 'Bike Products'


class CartItems(Base):
    bike_prod_id = models.ForeignKey(BikeProducts, on_delete=models.CASCADE, blank=True, default=1)
    quantity_sold = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{} - {}'.format(self.quantity_sold, str(self.bike_prod_id))

    class Meta:
        verbose_name_plural = 'Cart Items'


class Orders(Base):
    cust_id = models.ForeignKey(Customers, on_delete=models.CASCADE, blank=True, default=1)
    item_id = models.ManyToManyField(CartItems, blank=True, symmetrical=False)
    store_staff_id = models.ForeignKey(StoreEmployees, on_delete=models.CASCADE, blank=True, default=1)
    order_date = models.DateTimeField(auto_now_add=True)
    discount = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Orders'


class StockList(Base):
    #store_id = models.OneToOneField(Store, on_delete=models.CASCADE, blank=True, default=1)
    bike_prod_id = models.ManyToManyField(BikeProducts, symmetrical=False)
    quantity = models.PositiveIntegerField(default=0)

#models.setnull - keep children from dieing