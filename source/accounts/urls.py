from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from accounts.views import RegisterView, UserDetailView,  UserChangeView, UserPasswordChangeView

app_name = 'accounts'

urlpatterns = [

    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('create/', RegisterView.as_view(), name='create'),
    path('<int:pk>/', UserDetailView.as_view(), name='detail'),
    path('change/', UserChangeView.as_view(), name='change'),
    path('<int:pk>/password_change/', UserPasswordChangeView.as_view(), name='password_change'),

]