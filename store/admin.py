from django.contrib import admin
from .models import Store, Author, StoreCategory
# Register your models here.
admin.site.register(Store)
admin.site.register(StoreCategory)
admin.site.register(Author)