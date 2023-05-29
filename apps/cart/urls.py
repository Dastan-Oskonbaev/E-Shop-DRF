from django.urls import path
from .views import CartView, CartAddView, RemoveFromCartView

urlpatterns = [
    path('cart/', CartView.as_view(), name='cart'),
    path('cart/add/<int:product_id>/', CartAddView.as_view(), name='cart_add'),
    path('cart/remove/<int:product_id>/', RemoveFromCartView.as_view(), name='cart_remove'),
]
