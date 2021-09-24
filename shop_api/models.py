from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)
    
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

    def __str__(self):
        return self.name

class Image(models.Model):
    photo = models.ImageField(upload_to='images')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")

class Cart(models.Model):
    summ = models.IntegerField(default=0)
    owner = models.CharField(max_length=20)
    number = models.CharField(max_length=20)
    count = models.IntegerField()

class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, related_name="cart_products", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name="products", on_delete=models.CASCADE)




    




    

