from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Product
from .forms import QuestionForm
from questions.models import Question
from django.contrib import messages

def index(request):
    """
    목록 출력
    """
    product_list = Product.objects.order_by()
    context = {'product_list': product_list}
    return render(request, 'products/products_list.html', context)


def detail(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {'product': product}
    return render(request, 'products/products_detail.html', context)



def question_create(request, product_id):
    """
    질문등록
    """
    product = get_object_or_404(Product, pk=product_id)##혹시모르니바꿉시다
    product.question_set.create(body=request.POST.get('body'), user=request
                                .user, object_id = 2)

    return redirect('products:detail', product_id=product.id)


def question_create_save(request):

    form = QuestionForm()
    return render(request, 'products/products_form.html', {'form': form})




