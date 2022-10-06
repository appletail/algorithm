forms.py
```py
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ('author',)
```

views.py
```py
@require_safe
def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comment_form = CommentForm()
    comments = article.comment_set.all()
    context = {
        'article': article,
        'comment_form': comment_form,
        'comments': comments,

    }
    return render(request, 'articles/detail.html', context)

@require_http_methods(['GET', 'POST'])
@login_required
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)

@ require_POST
def comment_create(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.author = request.user
        comment.article = article
        comment.save()
        return redirect('articles:detail', article.pk)
    
    context = {
        'comment_form': comment_form,
    }
    return render(request, 'articles/detail.html', context)
```

detail.html
```html
  {% if request.user.is_authenticated %}
  <form action="{% url 'articles:create_comment' article.pk %}" method="POST">
    {% csrf_token %}
    {{ comment_form.as_p }}
    <button>댓글등록</button>
  </form>
  {% else %}
    <p>댓글을 등록하려면 로그인해주세요.</p>
  {% endif %}
```

models.py
```py
content = models.CharField(max_length=200, blank=True)
```