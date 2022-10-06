models.py
```py
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

forms.py
```py
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('author', 'article',)
```

urls.py
```py
    path('<int:pk>/comments/', views.comments_create, name='comments_create'),
    path('<int:article_pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete'),
```

views.py
```py
@require_safe
def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comments = article.comment_set.all()
    comments_form = CommentForm
    context = {
        'article': article,
        'comments': comments,
        'comments_form': comments_form,
    }
    return render(request, 'articles/detail.html', context)

@require_POST
def comments_create(request, pk):
    if request.user.is_authenticated:
        article = Article.objects.get(pk=pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.author = request.user
            comment.save()
        return redirect('articles:detail', article.pk)
    return redirect('accounts:login')

@require_POST
def comments_delete(request, article_pk, comment_pk):
    if request.user.is_authenticated:
        comment = Comment.objects.get(pk=comment_pk)
        if request.user == comment.author:
            comment.delete()
    return redirect('articles:detail', article_pk)

```

detail.html
```html
  {% if request.user == article.author %}
  <a href="{% url 'articles:update' article.pk %}">[UPDATE]</a>
  <form action="{% url 'articles:delete' article.pk %}" method="POST">
    {% csrf_token %}
    <button>DELETE</button>
  </form>
  {% endif %}
  <a href="{% url 'articles:index' %}">[back]</a>
  <hr>

  {% if request.user.is_authenticated %}
    <form action="{% url 'articles:comments_create' article.pk %}" method="POST">
      {% csrf_token %}
      {{ comments_form }}
      <input type="submit" value="댓글등록">
    </form>
  {% else %}
    <p>댓글은 로그인이 필요합니다.</p>
  {% endif %}

  <ul>
    {% for comment in comments %}
    <li>
      {{ comment.author }} - {{ comment.content }}
      {% if comment.author == request.user %}
        <form action="{% url 'articles:comments_delete' article.pk comment.pk %}" method="post">
          {% csrf_token %}
          <input type="submit" value="댓글삭제">
        </form>
      {% endif %}
    </li>
    {% empty %}
    <p>작성된 댓글이 없습니다.</p>
    {% endfor %}

  </ul>
```