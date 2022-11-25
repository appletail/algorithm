- models.py
```py
class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=10)
    content = models.TextField()
    hashtags = models.ManyToManyField(Hashtag, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
```

- urls.py
```py
    path('<int:hash_pk>/hashtag/', views.hashtag, name='hashtag'),
```

- views.py
```py
@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            for word in article.content.split():
                if word.startswith('#'):
                    hashtag = Hashtag.objects.get_or_create(content=word)
                    article.hashtags.add(hashtag[0])
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)


def hashtag(request, hash_pk):
    hashtag = Hashtag.objects.get(pk=hash_pk)
    articles = hashtag.article_set.order_by('-pk')
    context = {
        'hashtag': hashtag,
        'articles': articles,
    }
    return render(request, 'articles/hashtag.html', context)
```

- hashtag.html
```html
{% extends 'base.html' %}

{% block content %}
  <h1>{{ hashtag.content }}</h1>
  <p>{{ articles|length }}개의 게시글</p>
  <hr>
  <h1>{{ hashtag.content }}(을)를 태그한 글</h1>
  {% for article in articles %}
    <h2>{{ article.pk }}번 게시글</h2>
    <h2>{{ article.title }}</h2>
    <p>{{ article.comment_set.all|length }}개의 댓글</p>
    <br>
    <a href="{% url 'articles:detail' article.pk %}">상세글로 바로 가기</a>
    <hr>
  {% endfor %}

{% endblock content %}
```

- detail.html
```html
{% load make_link %}
  <p>내용 : {{ article.content|make_link|safe }}</p>
```

- make_link.py
```py
# articles/templatetags/make_link.py
from django import template
from articles.models import Hashtag

register = template.Library()

@register.filter
def make_link(content):
    content = content.split()
    
    for idx in range(len(content)):
        if content[idx].startswith('#'):
            hashtag = Hashtag.objects.get(content=content[idx])
            content[idx] = f'<a href="/articles/{hashtag.pk}/hashtag/">{hashtag.content}</a>'
    return ' '.join(content)
```