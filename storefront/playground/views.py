from django.db import reset_queries
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q, F, Value
from django.db.models.aggregates import Count, Min, Max, Avg
from store.models import Collection, Customer, OrderItem, Product, Order


def say_hello(request):

    # products = Product.objects.filter(unit_price__range=(20, 30))
    '''
    The following line does not work. Why?
    '''
    # query_set = Product.objects.filter(collection__id__range=(1, 2, 3))

    # query_set = Product.objects.filter(title__icontains='coffee')

    # query_set = Customer.objects.filter(email__iendswith='.com')

    # query_set = Collection.objects.filter(featured_product__isnull=True)

    # query_set = Product.objects.filter(inventory__lte=10)

    # query_set = Order.objects.filter(customer__id=1)

    # query_set = OrderItem.objects.filter(product__collection__id=3)

    # query_set = Product.objects.filter(
    #     Q(inventory__lt=10) | Q(unit_price__lt=20))

    # query_set = Product.objects.filter(description__icontains=F('title'))

    # query_set = Product.objects.order_by('-unit_price')[:10]

    # query_set = Product.objects.values('id', 'title', 'collection__title')

    # query_set = Product.objects.filter(id__in=OrderItem.objects.values(
    #     'product_id').distinct()).order_by('-title')

    # query_set = Order.objects.order_by(
    #     '-placed_at')[:5].select_related('customer').prefetch_related('orderitem_set')

    # products = list(query_set)

    # result = Order.objects.aggregate(total_orders=Count('id'))

    # result = OrderItem.objects.filter(
    #     product__id=1).aggregate(count=Count('id'))

    # result = Order.objects.filter(customer__id=1).aggregate(Count('id'))

    result = Product.objects.filter(collection__id=3).aggregate(
        min=Min('unit_price'), max=Max('unit_price'), average=Avg('unit_price'))

    return render(request, 'hello.html', {'name': 'Mosh', 'result': result})
