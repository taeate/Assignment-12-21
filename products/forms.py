from django import forms
from questions.models import Question


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question  # 사용할 모델
        fields = ['body']
        labels = {
            'subject': '제목',
            'content': '내용',
        }