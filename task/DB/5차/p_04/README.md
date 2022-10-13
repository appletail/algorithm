1. makemigrations 오류
```py
# models.py
like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')
```

2. 좋아요 오류
```py
# movies/views.py
@require_POST
def likes(request, movie_pk):
    if request.user.is_authenticated:
        movie = get_object_or_404(Movie, pk=movie_pk)

        if movie.like_users.filter(pk=request.user.pk).exists():
            # if request.user in movie.like_users.all():
            movie.like_users.remove(request.user)
        else:
            movie.like_users.add(request.user)
        return redirect("movies:index")
    return redirect("accounts:login")

# remove와 add를 서로 교환
```
3. 팔로우 오류
```html
<!-- accounts/profile.html -->
  {% if request.user != person %}
    <div>
      <form action="{% url 'accounts:follow' person.pk %}" method="POST">
        {% csrf_token %}
        {% if user in person.followers.all %}
          <button class="btn btn-outline-primary btn-sm">팔로우 취소</button>
        {% else %}
          <button class="btn btn-primary btn-sm">팔로우</button>
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