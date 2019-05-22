from django.db import models
from django.contrib.auth.models import User

CATEGORY_CHOICES = (
    ('Electronic', 'Electronic'),
    ('Cloth', 'Cloth'),
    ('Kid', 'Kid'),
)

SUB_CATEGORY_CHOICES = (
    ('Mobile', 'Mobile'),
    ('TV', 'TV'),
    ('Shirt', 'Shirt'),
    ('Pant', 'Pant'),
    ('Toy', 'Toy'),
    ('Book', 'Book'),
)


class Category(models.Model):
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.category


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=20, choices=SUB_CATEGORY_CHOICES)

    def __str__(self):
        return self.title


class Product(models.Model):
    merchant = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    price = models.IntegerField()
    quantity = models.IntegerField()
    added_date = models.DateTimeField(auto_now_add=True, null=True)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, default='Mobile')

    def __str__(self):
        return self.name


class Tags(models.Model):
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    product = models.OneToOneField(Product, on_delete=models.CASCADE, default=1)
    size = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    weight = models.CharField(max_length=20)

    def __str__(self):
        return self.sub_category


class ProductImages(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField()
