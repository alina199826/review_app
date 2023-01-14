from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404
from django.views.generic import  DeleteView, ListView,  CreateView, UpdateView
from django.urls import  reverse
from webapp.models import Review, Product
from webapp.forms import ReviewForm

class ReviewCreateView(LoginRequiredMixin, CreateView):
    template_name = 'rating_create.html'
    model = Review
    form_class = ReviewForm

    def get_success_url(self):
        return reverse('webapp:view', kwargs={'pk': self.object.product.pk})

    def form_valid(self, form):
        product = get_object_or_404(Product, pk=self.kwargs.get('pk'))
        form.instance.product = product
        form.instance.author = self.request.user
        return super().form_valid(form)


class ReviewIndexView(ListView):
    template_name = 'product_view.html'
    context_object_name = 'reviews'
    model = Review
    ordering = ('-created_at',)

class ReviewUpdateView(PermissionRequiredMixin, UpdateView):
    model = Review
    template_name = 'review_update.html'
    form_class = ReviewForm
    context_object_name = 'review'
    permission_required = 'webapp.change_review'

    def has_permission(self):
        return self.request.user.has_perm('webapp.change_review') or self.get_object().user == self.request.user

class ReviewDeleteView(UserPassesTestMixin, DeleteView):
    model = Review
    permission_required = 'webapp.delete_review'

    def has_permission(self):
        return self.request.user.has_perm('webapp.delete_review') or self.get_object().user == self.request.user


    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('webapp:product_view', kwargs={'pk': self.object.product.pk})


