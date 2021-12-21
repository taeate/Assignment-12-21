from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from products.models import *
# Create your models here.
from accounts.models import User


class Question(models.Model):
    reg_date = models.DateTimeField('등록날짜', auto_now_add=True)
    update_date = models.DateTimeField('갱신날짜', auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, related_name="content_type_question", on_delete=models.DO_NOTHING,null=True)
    object_id = models.PositiveIntegerField('관련 데이터 번호')
    content_object = GenericForeignKey('content_type', 'object_id')
    subject = models.CharField(max_length=50,null=True)##얘도 똑같이 널 허용
    body = models.TextField('내용')
    is_complete = models.BooleanField('답변완료여부', default=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    ##일단 강사님이 생성해둔 question데이타가 있는데 그값들은 현재
    ##product 속성이 비어있는 상태거든여
    ##근데 포린키는 무조건 값을 필요로 하는 상태에여
    ##그런데 지금당장 넣을 수가 없으니까
    ##널 허용한다는 뜻으로 null=True S2
    ##그리고 모델링이 변경되었으니까 migrate
    ##이제 이런경우 어디서 문제가 발생했는지부터 파악


class Answer(models.Model):
    reg_date = models.DateTimeField('등록날짜', auto_now_add=True)
    update_date = models.DateTimeField('갱신날짜', auto_now=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField('내용')
