models.py
```py
author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
```

views.py
```py
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.user.is_authenticated:
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
    else:
        return redirect('accounts:login')
```

forms.py
```py
from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ('author',)
```

detail.html
```html
  <p>작성자 : {{ article.author }}</p>
```