from django.urls import path

from . import views

app_name = 'cart'

urlpatterns = [
    path('add/<int:product_id>/', views.add, name='add'),
    path('basket_list/', views.basket_list, name='basket'),
]