from django.db import models
from django.contrib.auth.models import User 




# Create your models here.

class Address(models.Model):
    home_address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
    

class Userdetails(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=6)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True, blank=True)



class Service(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=False)


class LaptopBrand(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Technician(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True,blank=True)
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100)
    is_staff = models.BooleanField(default=True)  # Add the is_staff field
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True, blank=True)
    is_available = models.BooleanField(default=True) 

    def __str__(self):
        return self.username


class Booking(models.Model):
    device_type_choices = [
        ('laptop', 'Laptop'),
        ('desktop', 'Desktop'),
    ]
    userdetails = models.OneToOneField(Userdetails, on_delete=models.CASCADE, null=True, blank=True)
    device_type = models.CharField(max_length=7, choices=device_type_choices)
    brand = models.CharField(max_length=50, null=True, blank=True)
    preferred_date = models.DateField(null=False, blank=False)
    preferred_time = models.TimeField(null=False, blank=False)
    selected_services = models.ManyToManyField(Service, blank=True)
    total_service_cost = models.DecimalField(max_digits=10, decimal_places=2)
    is_verified = models.BooleanField(default=False)
    razorpay_payment_id = models.CharField(max_length=100, null=True, blank=True)  # Add this field



class Payment(models.Model):
    user = models.ForeignKey(Userdetails, on_delete=models.CASCADE)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, blank=True, null=True)  # Change here
    payment_date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.BooleanField(default=False)
    product = models.ForeignKey('SecondHandProduct', on_delete=models.CASCADE, blank=True, null=True)  # Updated field

    def __str__(self):
        return f"Payment for {self.user.username} on {self.payment_date}"
    
    



class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=250)
    rating = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class SecondHandProduct(models.Model):
    CONDITION_CHOICES = (
        ('new', 'New'),
        ('used', 'Used'),
        ('refurbished', 'Refurbished'),
    )
    ACTION_CHOICES = (
        ('pending', 'Approval Pending'),
        ('approved', 'Approved'),
    )
    

    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    description = models.TextField()
    condition = models.CharField(max_length=20, choices=CONDITION_CHOICES)
    year = models.CharField(max_length=4)  
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images')
    added_by = models.ForeignKey(Userdetails, on_delete=models.CASCADE, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,  blank=True, null=True)
    is_picked_up = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.brand} - {self.model}"







class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(SecondHandProduct, through='CartItem')

    def __str__(self):
        return f"Cart for {self.user.username}"

class CartItem(models.Model):
    product = models.ForeignKey(SecondHandProduct, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.product.category} in {self.cart.user.username}'s cart"






class Deliveryboy(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True,blank=True)
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True, blank=True)


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(SecondHandProduct, through='WishlistItem')

    def __str__(self):
        return f"Wishlist for {self.user.username}"

class WishlistItem(models.Model):
    product = models.ForeignKey(SecondHandProduct, on_delete=models.CASCADE)
    wishlist = models.ForeignKey(Wishlist, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product.category} in {self.wishlist.user.username}'s wishlist"


class Order(models.Model):
    DELIVERY_STATUS_CHOICES = [
        ('Shipped', 'Shipped'),
        ('Out_for_delivery', 'Out for Delivery'),
        ('Delivered', 'Delivered'),
    ]

    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)
    user = models.ForeignKey(Userdetails, on_delete=models.CASCADE)
    product = models.ForeignKey(SecondHandProduct, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    delivery_status = models.CharField(max_length=20, choices=DELIVERY_STATUS_CHOICES, default='SH')

    def __str__(self):
        return f"Order ID: {self.id}"


class LeaveApplication(models.Model):
    staff = models.ForeignKey(Deliveryboy, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    number_of_days = models.PositiveIntegerField()
    reason = models.TextField()
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Approved', 'Approved')], default='Pending')

    def __str__(self):
        return f"Leave Application for {self.staff.full_name}"