from django.urls import path

from . import views

app_name = 'orders'

urlpatterns = [
    path('cart-summary/', views.get_cart_summary, name='cart_summary'),
    path('add-to-cart/', views.add_to_cart, name='cart_add'),
    path('delete-from-cart/', views.delete_from_cart, name='cart_delete'),
    path('process-order/', views.process_order, name='process_order')
]