from django.shortcuts import render

# Create your views here.

def price(request,thing,cnt):

    price_product = {"라면":980,"홈런볼":1500,"칙촉":2300,"식빵":1800}

    if price_product.get(thing):
        total = price_product.get(thing) * cnt
    else:
        total = None

    context = {
        "thing" : thing,
        "cnt" : cnt,
        "product_price" : price_product,
        "total" : total,
    }

    return render(request,'price.html',context)
