from django.contrib import admin
from product_master.models import Product
from product_master.models import ProductImages
from product_master.models import Category
from product_master.models import SubCategory
from product_master.models import Tags

admin.site.register(Product)
admin.site.register(ProductImages)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Tags)






