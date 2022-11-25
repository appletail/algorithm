# 1번 오류
```py
# articles/models.py
like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name = 'like_articles')

# like_users에 related_name 추가
```

# 2번 오류
```py
# articles/views.py
@require_POST
def likes(request, article_pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=article_pk)

        if article.like_users.filter(pk=request.user.pk).exists():
        # if request.user in article.like_users.all():
            article.like_users.remove(request.user)
        else:
            article.like_users.add(request.user)
        return redirect('articles:index')
    return redirect('accounts:login')

# remove와 add를 서로 교환
```

# 3번 오류
```html
<!-- accounts/profile.html -->
  {% if request.user != person %}
    <div>
      <form action="{% url 'accounts:follow' person.pk %}" method="POST">
        {% csrf_token %}
        {% if user in person.followers.all %}
          <button>Unfollow</button>
        {% else %}
          <button>Follow</button>
        {% endif %}
      </form>
    </div>
  {% endif %}

{% if request.user != person %} 추가
```
```py
# accounts/views.py
@require_POST
def follow(request, user_pk):
    if request.user.is_authenticated:
        person = get_object_or_404(get_user_model(), pk=user_pk)
        if person != request.user:
            if person.followers.filter(pk=request.user.pk).exists():
            # if request.user in person.followers.all():
                person.followers.remove(request.user)
            else:
                person.followers.add(request.user)
        return redirect('accounts:profile', person.username)
    return redirect('accounts:login')

# if person != request.user: 추가
```