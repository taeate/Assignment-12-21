from django import forms
from questions.models import Question


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question  # 사용할 모델
        fields = ['subject', 'body']

##우리가 저놈의 필드가 필요한거잖아요?
#그런데 저기엔 해당 내용이 없고 다른이름으로 되어있죠?
#그리고 subject가 없다면 question에 subject를 추가하고
#makemigrations migrate해주면되구여
#제목이란 옵션으로
#에러가 안떴쪄?
##product에 foreign키로 접근할 수 있는
##Question이 없데여
##Question에 foreign키로 Product를 넣어주면데여가마니
##저말은 프로덕트에는 저런 속성이 없단거고
##저런 속성이 없단건 안만들어졌단거