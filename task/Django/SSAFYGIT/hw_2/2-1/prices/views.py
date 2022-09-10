from django.shortcuts import render

# Create your views here.
def product(request, thing, cnt):
    product_price = {"라면":980,"홈런볼":1500,"칙촉":2300, "식빵":1800}
    price = product_price.get(thing)
    context = {
        'product': product_price,
        'thing': thing,
        'price': price,
        'cnt': cnt,
    }
    return render(request, 'price.html', context)