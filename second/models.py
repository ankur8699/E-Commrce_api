from django.db import models

# Create your models here.
CATEGORY_CHOICES = (
    ('Laptops', 'Laptops'),
    ('Desktops', 'Desktops'),
    ('Printers', 'Printers'),
    ('Survilliance', 'Survilliance'),
    ('LED TV', 'LED TV'),
    ('Tablets', 'Tablets'),
    ('Biometrics', 'Biometrice'),
    ('UPS', 'UPS'),
    ('Cables', 'Cables'),
    ('Accessories', 'Accessories'),
)


class Products(models.Model):
    Product_name=models.CharField(max_length=200,null=True)
    title = models.CharField(max_length=200)
    offers=models.TextField(null=True)
    price = models.FloatField()
    Image=models.ImageField(upload_to='media/',null=True)
    Delivery=models.CharField(max_length=10,null=True)
    Warranty=models.CharField(max_length=10,null=True)
    Description=models.TextField(null=True)
    Specifications=models.TextField(null=True)
    More_Info=models.TextField(null=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=20)
    FAQ=models.TextField(null=True)
    Brand=models.CharField(max_length=200,null=True)
    StockLeft=models.CharField(max_length=50,null=True)
    Color=models.CharField(max_length=100,null=True)
    def __unicode__(self):
        return self.title

class Details(models.Model):
    ids=models.ForeignKey(Products, on_delete=models.CASCADE, related_name='product_details', null=True , blank=True)
    image = models.ImageField(upload_to='media/')
    created_at = models.DateTimeField(auto_now_add=True)

class Images(models.Model):
    idi=models.ForeignKey(Products, on_delete=models.CASCADE, related_name='Images', null=True , blank=True)
    img = models.ImageField(upload_to='media/',null=True)
    img2 = models.ImageField(upload_to='media/',null=True)
    img3 = models.ImageField(upload_to='media/',null=True)
    img4 = models.ImageField(upload_to='media/',null=True)
    img5 = models.ImageField(upload_to='media/',null=True)
    