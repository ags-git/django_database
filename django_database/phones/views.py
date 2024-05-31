from django.shortcuts import render, redirect
from phones.models import Phone

# Create your views here.

def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sorting = {'sort=name': 'name',
               'sort=min_price': 'price',
               'sort=max_price': '-price'}

    if len(request.META['QUERY_STRING']) > 0:
        phones = Phone.objects.order_by(sorting[request.META['QUERY_STRING']])
    else:
        phones = Phone.objects.all()

    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {'phone': phone}
    return render(request, template, context)