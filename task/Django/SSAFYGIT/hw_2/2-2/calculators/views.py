from django.shortcuts import render

# Create your views here.
def calculators(request, num1, num2):
    if num2 != 0:
        nanugi = num1 / num2
    else:
        nanugi = 0
    context = {
        'num1': num1,
        'num2': num2,
        'num2_minus': -num2,
        'nanugi': nanugi,
    }
    return render(request, 'calculators/calculator.html', context)