from django.urls import path
from products import views


app_name = 'products'


urlpatterns = [
    path('list/', views.index, name="list"),
    path('<int:product_id>/', views.detail, name='detail'),
    path('question/create/<int:product_id>/', views.question_create, name='question_create'),
]

#님 푸시를안했었어여