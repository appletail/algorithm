from django.shortcuts import render, redirect
from django.views.decorators.http import require_safe, require_http_methods, require_POST
from .models import Article
from .forms import ArticleForm


# Create your views here.
@require_safe
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


@require_http_methods(['GET', 'POST'])
def create(request):
    # POST를 먼저 확인하는 이유: 메서드에는 GET과 POST말고 다양하게 있는데, GET인지 먼저 확인하면 else에서 수많은 메서드가 올때 모두 DB를 수정해버림 / 데코레이터가 있기에 GET과 POST만 들어올 수 있음
    if request.method == 'POST':  # create에 있던 코드
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:   # new에서 쓰이던 코드
        form = ArticleForm()
    context = {   # is_valid를 통과못하는 경우도 고려하여 들여쓰기를 밖에 둔 것
        'form': form,
    }
    return render(request, 'articles/create.html', context)


@require_safe
def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


@require_POST
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')


@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        # form = ArticleForm(data=request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/update.html', context)
