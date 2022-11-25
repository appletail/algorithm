from django.shortcuts import render

# Create your views here.
def first(request):
    catch = request.GET.get('catch')
    context = {
        'catch': catch,
    }
    return render(request, 'throw_catch/first.html', context)

def second(request):
    catch = request.GET.get('catch')
    context = {
        'catch': catch,
    }
    return render(request, 'throw_catch/second.html', context)
