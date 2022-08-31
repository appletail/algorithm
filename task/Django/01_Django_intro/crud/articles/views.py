from django.shortcuts import render
from .models import Article
# Create your views here.
def index(request):
    # DB에 전체 데이터를 조회
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    # 사용자의 데이터를 받아서 DB에 저장
    get_title = request.GET.get('title')
    content = request.GET.get('content')


    # DB에 저장

    # 1번 방법 _안쓰는 이유: 2번보다는 길어서 안씀
    # article = Article()
    # article.title = get_title  # 보통은 이름을 똑같이 하는데 헷갈리지 마라고 get_title 사용
    # article.content = content
    # article.save()

    # 2번 방법 _주로 사용: save 전까지 조작하고 검증 가능
    article = Article(title = get_title, content = content)
    # 유효성 검사 등

    article.save()

    # 3번 방법 _안쓰는 이유: 바로 저장되기 때문에 검증 불가
    # Article.objects.create(title=get_title, content = content)

    return render(request, 'articles/create.html')