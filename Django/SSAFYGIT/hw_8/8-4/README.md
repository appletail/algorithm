- 화면 상단에 이미지 출력
```html
<!-- base.html -->
    <img src=" {% static 'images/django.png' %}" alt="image">

<!-- images/django.png 로 수정 -->
```
```py
# settings.py
STATICFILES_DIRS = [
    BASE_DIR / 'static'
]
# statics -> static로 오타 수정
```
- create 기능 수행시 오류
- a. 사진이 올라가지 않음
```py
# views.py
form = ArticleForm(request.POST, request.FILES)
# request.FILES 추가
```

- b. 사진이 보이지 않음
```html
<!-- deatil.html -->
<img src="{{ article.image.url }}" alt="image">
<!-- {{ article.image.url }} 중괄호 추가 -->
```