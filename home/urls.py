from django.urls import path
from home import views

app_name = 'home'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('base/',views.base, name='base'),
    path('others/', views.others, name='others'),
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login'),
]