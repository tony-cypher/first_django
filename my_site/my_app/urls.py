from my_app import views
from django.urls import path

app_name = 'my_app'

urlpatterns = [
    path('login/', views.user_login, name='user_login'),
    path('register/', views.register, name='register'),
]