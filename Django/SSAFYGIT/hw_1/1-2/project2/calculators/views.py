from django.shortcuts import render

# Create your views here.
def calculation(request):
    return render(request, 'calculation.html')

def result(request):
    number_one = request.GET.get('number_one')
    number_two = request.GET.get('number_two')
    multiplication = int(number_one) * int(number_two)
    subtraction = int(number_one) - int(number_two)
    if int(number_two) != 0:
        division = int(number_one) / int(number_two)
    else:
        division = 0

    context = {
        'number_one': number_one,
        'number_two': number_two,
        'multiplication': multiplication,
        'subtraction': subtraction,
        'division': division,
    }

    return render(request, 'result.html', context)