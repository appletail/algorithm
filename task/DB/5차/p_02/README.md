# 프로필 페이지
- urls.py
```py
# accounts/urls.py
path('<str:username>/', views.profile, name='profile'),
```

- views.py
```py
# accounts/urls.py
from django.contrib.auth import get_user_model


def profile(request, username):
    User = get_user_model()
    person = User.objects.get(username=username)
    context = {'person': person,}
    return render(request, 'accounts/profile.html', context)
```


- profile.html
```html
<!-- templates/accounts/profile.html -->
{% extends 'base.html' %}

{% block content %}
  <h1>{{ person.username }}님의 프로필</h1>
  <hr>
  <h2>{{ person.username }}'s 게시글</h2>
  {% for movie in person.movie_set.all %}
    <p>{{ movie.title}} </p>
  {% endfor %}
  <hr>
  <h2>{{ person.username }}'s 댓글</h2>
  {% for comment in person.comment_set.all %}
    <p>{{ comment.content }}</p>
  {% endfor %}
  <hr>
  <a href="{% url 'movies:index' %}" class="btn btn-secondary btn-sm">이전</a>
  
{% endblock content %}
```

# 팔로우 구현
- models.py
```py
# accounts/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
```

- urls.py
```py
# templates/accounts/urls.py
    path('<int:user_pk>/follow/', views.follow, name='follow'),
```

- views.py
```py
# accounts/views.py
def follow(request, user_pk):
    if request.user.is_authenticated:
        you = get_user_model().objects.get(pk=user_pk)
        me = request.user
        if you != me:
            if you.followers.filter(pk=me.pk).exists():
                you.followers.remove(me)
            else:
                you.followers.add(me)
        return redirect('accounts:profile', you.username)
    return redirect('accounts:login')
```

- profile.html
```html
<!-- templates/accounts/profile.html -->
{% extends 'base.html' %}

{% block content %}
  <h1>{{ person.username }}님의 프로필</h1>
  <p>팔로잉 : {{ person.followings.all | length }} / 팔로워 : {{ person.followers.all | length }}</p>
  {% if request.user != person %}
  <form action="{% url 'accounts:follow' person.pk %}" method="post">
    {% csrf_token %}
    {% if request.user in person.followers.all %}
      <input type="submit" value="팔로우 취소" class="btn btn-outline-primary btn-sm">
      {% else %}
      <input type="submit" value="팔로우" class="btn btn-outline-primary btn-sm">
    {% endif %}
  </form>
  
  {% endif %}
  <hr>
  <h2>{{ person.username }}'s 게시글</h2>
  {% for movie in person.movie_set.all %}
    <p>{{ movie.title}} </p>
  {% endfor %}
  <hr>
  <h2>{{ person.username }}'s 댓글</h2>
  {% for comment in person.comment_set.all %}
    <p>{{ comment.content }}</p>
  {% endfor %}
  <hr>
  <a href="{% url 'movies:index' %}" class="btn btn-secondary btn-sm">이전</a>
  
{% endblock content %}
```