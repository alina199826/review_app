from django.contrib.auth.mixins import  PermissionRequiredMixin

from webapp.models import Product
from webapp.forms import ProductForm
from django.views.generic import DeleteView, ListView, DetailView, CreateView, UpdateView

from django.urls import reverse_lazy


class IndexViews(ListView):
    template_name = 'index.html'
    context_object_name = 'products'
    model = Product
    ordering = ('category', 'title')

class ProductView(DetailView):
    template_name = 'product_view.html'
    model = Product


class ProductCreateView(PermissionRequiredMixin, CreateView):
    template_name = "product_create.html"
    model = Product
    form_class = ProductForm
    permission_required = 'webapp.add_product'




class ProductUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = "product_update.html"
    form_class = ProductForm
    model = Product
    context_object_name = 'product'
    permission_required = 'webapp.change_product'



class ProductDeleteView(PermissionRequiredMixin, DeleteView):
    model = Product
    template_name = "product_delete.html"
    success_url = reverse_lazy('webapp:index')
    permission_required = 'webapp.delete_product'


