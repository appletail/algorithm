from django.shortcuts import render

# Create your views here.
def first(request):
    third_catch = request.GET.get('third', 'nothing')
    context = {
        'third_catch': third_catch
    }
    return render(request, 'first.html', context)

def second(request):
    first_catch = request.GET.get('first')
    context = {
        'first_catch': first_catch
    }
    return render(request, 'second.html', context)
    
def third(request):
    first_catch = request.GET.get('first')
    second_catch = request.GET.get('second')
    catch = [first_catch, second_catch]
    context = {
        'catch': catch,
    }
    return render(request, 'third.html', context)