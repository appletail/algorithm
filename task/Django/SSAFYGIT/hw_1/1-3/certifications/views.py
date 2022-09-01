from django.shortcuts import render

# Create your views here.
age = range(25, 31)
grade = ['a', 'b', 'c', 's']

def certification1(request):
    context = {
        'age': age,
        'grade': grade,
    }
    return render(request, 'certification1.html', context)

def certification2(request):
    context = {
        'age': age,
        'grade': grade,
    }
    return render(request, 'certification2.html', context)

def certification3(request):
    context = {
        'age': age,
        'grade': grade,
    }
    return render(request, 'certification3.html', context)