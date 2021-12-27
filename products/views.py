from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Product
from .forms import QuestionForm
from questions.models import Question
from django.contrib import messages
from django.core import exceptions
from django.contrib.auth.decorators import login_required


def index(request):
    """
    목록 출력
    """
    product_list = Product.objects.order_by()
    context = {'product_list': product_list}
    return render(request, 'products/products_list.html', context)


def detail(request, product_id):
    product = Product.objects.get(id=product_id)
    questions = Question.objects.filter(
        object_id=product_id).filter(content_type=ContentType.objects.get(app_label='products', model='product'))
    context = {'product': product, 'questions': questions}
    return render(request, 'products/products_detail.html', context)


def question_create(request, product_id):
    """
    질문 등록
    """
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.object_id = product_id
            question.content_type = ContentType.objects.get(app_label='products', model='product')
            question.save()
            return redirect('products:detail', product_id=product_id)
    else:
        form = QuestionForm()
    return redirect('products:detail', product_id=product_id)


@login_required(login_url='accounts:login')
def question_modify(request, product_id, question_id):
    """
    질문 댓글 수정
    """
    question = get_object_or_404(Question, pk=question_id)
    product = get_object_or_404(Product, pk=product_id)
    if request.user != question.user:
        messages.error(request, '댓글 수정권한이 없습니다')
        return redirect('products:detail', product_id=product_id)

    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.modify_date = timezone.now()
            question.save()

            context = {'form': form, 'product': product}
            return redirect('products:detail', product_id=product.id)
    else:
        form = QuestionForm(instance=question)
    context = {'form': form, 'question': question, 'product': product}
    return render(request, 'products/question_form.html', context)


@login_required(login_url='accounts:login')
def question_delete(request, product_id, question_id):
    """
    질문 삭제
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.user:
        raise exceptions.PermissionDenied()
    question.delete()
    messages.success(request, "질문이 삭제되었습니다.")
    return redirect('products:detail', product_id=product_id)
