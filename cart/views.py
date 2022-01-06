from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from cart.forms import CartAddForm
from cart.models import CartItem
from products.models import ProductReal

@login_required
def add(request: HttpRequest, product_id):
    if request.method == "POST":
        product_real_id = request.POST.get('product_real')
        product_real = ProductReal.objects.get(id=product_real_id)
        form = CartAddForm(request.POST, product_id=product_real.product_id)

        if form.is_valid():
            cart_item = form.save(commit=False)
            cart_item.user = request.user
            cart_item.save()

            messages.success(request, "장바구니에 추가되었습니다.")
            return redirect('products:detail', product_id=product_id)



def basket_list(request):

    cart_items = CartItem.objects.filter(user=request.user)
    context = {'cart_items': cart_items}

    return render(request, 'cart_list.html',  context)