# toggle
```py
# urls.py
path('<int:pk>/', views.toggle, name='toggle'),

# views.py
def toggle(request, pk):
    todo = Todo.objects.get(pk=pk)
    if request.user.is_authenticated:
        if request.user == todo.author:
            if request.method == 'POST':
                if todo.completed:
                    todo.completed = 0
                else:
                    todo.completed = 1
                todo.save()
        return redirect('todos:index')
    else:
        return redirect('accounts:login')
```
토글
![index1](index1.PNG)
![index2](index2.PNG)

# delete
```py
# urls.py
path('<int:pk>/delete/', views.delete, name='delete'),

# views.py
def delete(request, pk):
    todo = Todo.objects.get(pk=pk)
    if request.user.is_authenticated:
        if request.user == todo.author:
            if request.method == 'POST':
                todo.delete()
        return redirect('todos:index')
    else:
        return redirect('accounts:login')
```
삭제표시
![index2](index2.PNG)
비로그인시
![index2](index3.PNG)

index.html
```html
  <ul>
  {% for todo in todos %}
    <li>{{ todo.author }} - {{ todo.title }}</li>
    {% if request.user == todo.author %}
      <form action="{% url 'todos:toggle' todo.pk %}" method="post">
        {% csrf_token %}
        {% if todo.completed == 1 %}
          <input type="submit" value="취소하기">
        {% else %}
          <input type="submit" value="완료하기">
        {% endif %}
      </form>
      <form action="{% url 'todos:delete' todo.pk %}" method="post">
        {% csrf_token %}
        <input type="submit" value="삭제하기">
      </form>
    {% endif %}
  {% empty %}
     <p>작성된 글이 없습니다.</p>
  {% endfor %}
  </ul>
```