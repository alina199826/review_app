
from django.urls import path
from webapp.views.product_views import IndexViews, ProductView, ProductDeleteView, ProductUpdateView, ProductCreateView
from webapp.views.review_views import ReviewCreateView
from django.views.generic import RedirectView

app_name = 'webapp'

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='webapp:index')),
    path('product/', IndexViews.as_view(), name='index'),
    path('product/<int:pk>/', ProductView.as_view(), name='view'),
    path('product/add/', ProductCreateView.as_view(), name='create'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='delete'),
    path('product/<int:pk>/add_review/', ReviewCreateView.as_view(), name='rating_create'),


]