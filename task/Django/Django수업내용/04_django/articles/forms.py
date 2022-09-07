from django import forms
from .models import Article

# forms 클래스는 굳이 forms.py이름으로 안만들어도 되고, models.py 같은 곳 등 어디에나 작성 가능 / 유지보수와 관행적으로 forms.py에 작성하는 것

# Form: DB와 연관없이 단순 데이터만 사용되는 경우에 주로 사용, Model과 별개임
# ex) 로그인, 사용자의 데이터를 받아 인증 과정에서만 사용 후 별도로 DB에 저장하지 않는 경우 등
# class ArticleForm(forms.Form):
#     드랍다운 형태로 다른 정보 받는 방식
    #   실제로받는 데이터
    #   NATION_? 식으로 나눠서 작성하는 이유: 장고 스타일 가이드 권장사항임
#     NATION_A = 'kr'
#     NATION_B = 'ch'
#     NATION_C = 'jp'
    #   사용자에게 보이는 글자
#     NATIONS_CHOICES = [
#         (NATION_A, '한국'),
#         (NATION_B, '중국'),
#         (NATION_C, '일본'),
#     ]

#     title = forms.CharField(max_length=10)
        # max_legnth: models에서와는 달리 필수는 아님 / 기본 input은 text임

#     content = forms.CharField(widget=forms.Textarea)
        # forms에서는 텍스트 필드(큰 문자열을 받는 필드)가 없음 / widget으로 input 방식을 바꿀 수 있음

#     nation = forms.ChoiceField(choices=NATIONS_CHOICES)
#     nation = forms.ChoiceField(choices=NATIONS_CHOICES, widget=forms.RadioSelect)
#     ChoicesField


# ModelForm: DB와 연관되어 있는 경우에 사용, Model에 종속되어 있음
class ArticleForm(forms.ModelForm):

    class Meta:  # 모델폼에 대한 데이타를 작성한다고 하여 Meta라 이름 지음
        model = Article
        fields = '__all__'  # __all_ : 사용자로부터 입력받는 모든 필드
        # exclude = ('title',)  # fields 대신 이것만 쓰는 경우 이것만 제외하고 나머지만 받게 됨

# 모델 폼은 모델에 맞추어 형식을 바꿔줌 ex) 위젯없이 인풋을 textarea로 만들어줌
# models와 fields 변수명은 바꾸면 안됨