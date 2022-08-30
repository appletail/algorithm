from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def greeting(request):
    family = ['Tom', 'Mom', 'Dad']
    context = {
        'name': 'Alice', 
        'age': 25, 
        'family': family
    }
    return render(request, 'greeting.html', context)

def dinner(request):
    foods = [
        '가지덮밥', 
        '차돌된장찌개', 
        '오리주물럭', 
        '열무국수',
    ]
    context = {'foods': foods}
    return render(request, 'dinner.html', context)

def throw(request):
    return render(request, 'throw.html')

def catch(request):
    message = request.GET.get('message')
    mas = request.GET.get('ma2')
    context = {
        'message1': message,
        'message2': mas,
    }
    print(request)
    print(type(request))

    return render(request, 'catch.html', context)

def hello(request, name):
    context = {
        'name': name
    }
    return render(request, 'hello.html', context)