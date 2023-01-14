from django.contrib import admin

# Register your models here.
from django.contrib import admin

from webapp.models import Product, Review
# Register your models here


class ProductAdmin(admin.ModelAdmin):
     list_display = ['title',  'category', 'description', 'img']
     search_fields = ['title']
     exclude = []


class ReviewAdmin(admin.ModelAdmin):
     list_display = ['text', 'rating', 'modern']
     readonly_fields = ['created_at', 'updated_at']
     exclude = []


admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)
