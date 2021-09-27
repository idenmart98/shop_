from django.db import models

CREATED = "CREATED"
PENDING = "PENDING"
IN_WAY = "IN_WAY"
DONE = "DONE"

CART_CHOICES = (
    (CREATED, "Created"),
    (PENDING, "Pending"),
    (IN_WAY, "In way"),
    (DONE, "Done")
)

class Category(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=3, decimal_places=2)
    description = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    count = models.IntegerField(default=0)
    sell = models.IntegerField(default=0)
    booked = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

class Image(models.Model):
    photo = models.ImageField(upload_to='images')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")

class Cart(models.Model):
    summ = models.IntegerField(default=0)
    owner = models.CharField(max_length=20)
    number = models.CharField(max_length=20)
    count = models.IntegerField(default=0)
    status = models.CharField(max_length=10, choices=CART_CHOICES, default=CREATED)
    created = models.DateTimeField(auto_now_add=True)

class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, related_name="cart_products", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name="products", on_delete=models.CASCADE)




    




    

