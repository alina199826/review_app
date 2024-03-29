from django import forms
from webapp.models import Product, Review

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'img', 'category']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [ 'text', 'product', 'rating', 'modern']