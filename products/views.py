from django.shortcuts import render
from .models import Products


# Create your views here.


def product_detail_view(request):
    obj = Products.objects.get(id=1)
    # context = {
    #     "title": obj.title,
    #     "description": obj.description,
    #     "summary": obj.summary
    # }
    context = {
        'object': obj
    }

    return render(request, "product/detail.html", context)
