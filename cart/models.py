from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
from accounts.models import User
from products.models import ProductReal


class CartItem(models.Model):
    reg_date = models.DateTimeField('등록날짜', auto_now_add=True)
    update_date = models.DateTimeField('갱신날짜', auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_real = models.ForeignKey(ProductReal, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField('수량', default=1,
                                           validators=[MinValueValidator(1), MaxValueValidator(10)])
