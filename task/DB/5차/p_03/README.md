- models.py
```py
class Hashtag(models.Model):
    content = models.CharField(max_length = 20, unique=True)


class Movie(models.Model):
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="like_movies"
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    hashtags = models.ManyToManyField(Hashtag, blank=True)

    def __str__(self):
        return self.title
```

- urls.py
```py
    path("<int:hash_pk>/hashtag/", views.hashtag, name="hashtag"),
```

- views.py
```py
@login_required
@require_http_methods(["GET", "POST"])
def create(request):
    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.user = request.user
            movie.save()
            for word in movie.content.split():
                if word.startswith('#'):
                    hashtag = Hashtag.objects.get_or_create(content=word)
                    movie.hashtags.add(hashtag[0])
            return redirect("movies:detail", movie.pk)
    else:
        form = MovieForm()
    context = {
        "form": form,
    }
    return render(request, "movies/create.html", context)


@login_required
@require_http_methods(["GET", "POST"])
def update(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.user == movie.user:
        if request.method == "POST":
            form = MovieForm(request.POST, instance=movie)
            if form.is_valid():
                movie = form.save()
                movie.hashtags.clear()
                for word in movie.content.split():
                    if word.startswith('#'):
                        hashtag = Hashtag.objects.get_or_create(content=word)
                        movie.hashtags.add(hashtag[0])

                return redirect("movies:detail", movie.pk)
        else:
            form = MovieForm(instance=movie)
    else:
        return redirect("movies:index")
    context = {
        "movie": movie,
        "form": form,
    }
    return render(request, "movies/update.html", context)


@require_safe
def hashtag(request, hash_pk):
    hashtag = Hashtag.objects.get(pk=hash_pk)
    movies = hashtag.movie_set.order_by('-pk')
    context = {
        'hashtag': hashtag,
        'movies': movies,
    }
    return render(request, 'movies/hashtag.html', context)
```

- hashtag.html
```html
{% extends 'base.html' %}

{% block content %}
  <h1>{{ hashtag.content }}</h1>
  <p>{{ movies|length }}개의 게시글</p>
  <hr>
  <h1>{{ hashtag.content }} (을)를 태그한 글</h1>
  <br>
  {% for movie in movies %}
    <h5>영화 {{ movie.title }}</h4>
    <p>{{ movie.comment_set.all|length }}개의 댓글</p>
    <a href="{% url 'movies:detail' movie.pk %}" class="btn btn-primary btn-sm">상세글로 바로 가기</a>
    <hr>
  {% endfor %}
{% endblock content %}
```

- detail.html
```html
{% load bootstrap5 make_link %}

  <p>{{ movie.content|hashtag|safe }}</p>
```

- make_link.py
```py
# movies/templatetags/make_link.py
from django import template
from movies.models import Hashtag

register = template.Library()

@register.filter
def hashtag(content):
    content = content.split()

    for idx in range(len(content)):
        if content[idx].startswith('#'):
            hashtag = Hashtag.objects.get(content=content[idx])
            content[idx] = f'<a href="/movies/{hashtag.pk}/hashtag">{hashtag.content}</a>'
    return ' '.join(content)
```