from django.shortcuts import redirect, render
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
    get_title = request.POST.get('title')
    content = request.POST.get('content')


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

    return redirect('articles:detail', article.pk)
    # return redirect('/articles/')  # index의 path가 ''라서 가능
    # , 후에 article.pk 쓰는 이유는 redirect가 그냥 그런 식으로 정의된 함수이기 때문

def detail(request, pk):
    article = Article.objects.get(pk=pk)  # 앞의 pk: 테이블의 필드 / 뒤의 pk: 파라미터의 pk
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')


def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/edit.html', context)

def update(request, pk):
    title = request.POST.get('title')
    content = request.POST.get('content')

    article = Article.objects.get(pk=pk)
    article.title = title
    article.content = content
    article.save()
    
    return redirect('articles:detail', article.pk)
