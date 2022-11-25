models.py
```py
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name = 'like_articles')
```

urls.py
```py
 path('<int:article_pk>/likes/', views.like, name='like'),
```


view.py
```py
def like(request, article_pk):
    if request.user.is_authenticated:
        article = Article.objects.get(pk=article_pk)
        if article.like_users.filter(pk=request.user.pk).exists():
            article.like_users.remove(request.user)
        else:
            article.like_users.add(request.user)
        return redirect('articles:index')
    
    return redirect('accounts:login')
```

index.html
```html
    <form action="{% url 'articles:like' article.pk %}" method="post">
      {% csrf_token %}
      {% if request.user in article.like_users.all %}
        <input type="submit" value="좋아요 취소">
      {% else %}
        <input type="submit" value="좋아요">
      {% endif %}
    </form>
    <p>{{ article.like_users.all | length }} 명이 이 글을 좋아합니다.</p>
```