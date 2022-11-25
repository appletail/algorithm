- models.py
```py
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')
```

- urls.py
```py
path('<int:movie_pk>/likes/', views.likes, name='likes'),
```

- views.py
```py
@require_POST
def likes(request, movie_pk):
    if request.user.is_authenticated:
        movie = Movie.objects.get(pk=movie_pk)
        user = request.user
        if movie.like_users.filter(pk=user.pk).exists():
            movie.like_users.remove(user)
        else:
            movie.like_users.add(user)
        return redirect('movies:index')
    return redirect('accounts:login')
```

- index.html
```html
    <form action="{% url 'movies:likes' movie.pk %}" method="post">
      {% csrf_token %}
      {% if request.user in movie.like_users.all %}
        <input type="submit" value="좋아요 취소" class="btn btn-primary btn-sm">
        {% else %}
        <input type="submit" value="좋아요" class="btn btn-primary btn-sm">
      {% endif %}
    </form>
    <p>{{ movie.like_users.all | length }} 명이 이 글을 좋아합니다.</p>
```