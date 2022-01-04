from django.forms import Form

from cart.models import CartItem


class CartAddForm(Form):
    class Meta:
        model = CartItem
        fields = ['product_real_id', 'quantity']