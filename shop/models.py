from django.db import models

# Create your models here.


class Product(models.Model):
    ID=models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name="Prodect Name ")
    Description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    Image = models.ImageField(upload_to='products/', null=True, blank=True)
    stock = models.IntegerField(default=0, verbose_name="Stock Quantity")
   
    def __str__(self):
        return self.name

class Customer(models.Model):
    ID=models.AutoField(primary_key=True)
    fname = models.CharField(max_length=50, verbose_name="First name")
    mname = models.CharField(max_length=50, blank=True, null=True, verbose_name="middle name")
    lname = models.CharField(max_length=50, verbose_name="Last name")
    phone = models.CharField(max_length=12, unique=True,verbose_name="Phone Numer" )
    Email = models.EmailField(unique=True)
    Address = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.fname} {self.lname} ({self.ID})"

class Order(models.Model):
     ID=models.AutoField(primary_key=True)
     customer_name=models.CharField(max_length=100, verbose_name="Customer Name")
     customer_id = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name='orders',
        verbose_name="Customer_id"
    )
   
     order_date = models.DateTimeField(auto_now_add=True, verbose_name="Order Date")
  
   
     STATUS_CHOICES = [
        ('Pending','Pending'),
        ('Processing','Processing'),
        ('Shipped','Shipped'),
        ('Delivered','Delivered'),
    ]
     status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending',
        verbose_name="Order Status "
    )
   
     total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name="Total Price")
   
   

     def __str__(self):
        return f"Order #{self.ID} by {self.customer_id.fname}"

class OrderItem(models.Model):
     ID=models.AutoField(primary_key=True)
     order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='items',
        verbose_name="Order item"
    )
   
     product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,

    )
   
     quantity = models.IntegerField(default=1, verbose_name="Quantity")
   
     price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price")

     def __str__(self):
        return f"{self.quantity} x {self.product.name} in Order #{self.order.ID}"



