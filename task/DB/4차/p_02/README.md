models.py
```py
# 팔로우
class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name = 'followers')
```

urls.py
```py
# 프로필
    path('<str:username>/', views.profile, name='profile'),
# 팔로우
    path('<int:user_pk>/follow/', views.follow, name='follow'),
```

views.py
```py
# 프로필
def profile(request, username):
    User = get_user_model()
    person = User.objects.get(username=username)
    context = {
        'person': person,
    }
    return render(request, 'accounts/profile.html', context)


# 팔로우
def follow(request, user_pk):
    if request.user.is_authenticated:
        User = get_user_model()
        you = User.objects.get(pk=user_pk)
        me = request.user
        if me != you:
            if you.followers.filter(pk=me.pk).exists():
                you.followers.remove(me)
            else:
                you.followers.add(me)
            return redirect('accounts:profile', you.username)
    return redirect('accounts:login')
```

profile.html
```html
{% extends 'base.html' %}

{% block content %}
<h1>{{ person.username }}님의 프로필</h1>
<p>팔로잉 : {{ person.followings.all | length }} / 팔로워 : {{ person.followers.all | length }}</p>
{% if request.user != person %}
  {% if request.user in person.followers.all %}
    <form action="{% url 'accounts:follow' person.pk %}" method="post">
      {% csrf_token %}
      <input type="submit" value="언팔로우"></form>
  {% else %}
    <form action="{% url 'accounts:follow' person.pk %}" method="post">
      {% csrf_token %}
      <input type="submit" value="팔로우"></form>
  {% endif %}

{% endif %}
<hr>
<h2>{{ person.username }}'s 게시글</h2>
{% for article in person.article_set.all %}
  <p>{{ article.pk }}</p>
  <p>{{ article.title }}</p>
{% endfor %}
<hr>
<h2>{{ person.username }}'s 댓글</h2>
{% for comment in person.comment_set.all %}
  <p>{{ comment.pk }}</p>
  <p>{{ comment.content }}</p>
{% endfor %}
<hr>
<a href="{% url 'articles:index' %}">back</a>

{% endblock content %}
```