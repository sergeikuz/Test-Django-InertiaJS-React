from django.views import View
from django.views.generic import ListView, DetailView
from inertia import render
from inertia import location
from .models import Product
import logging

logger = logging.getLogger(__name__)


def index(request):
    return render(request, "Index", props={"description": "Демо Django + InertiaJS + React"})


def about(request):
    return render(request, "About", props={"description": "Демо Django + InertiaJS + React, для лучшего понимания SPAшки"})


class ProductsListView(ListView):
    model = Product
    paginate_by = 4

    def get(self, request, *args, **kwargs):
        products = self.get_queryset()
        paginator = self.get_paginator(products, self.paginate_by)
        current_page = self.request.GET.get('page', 1)
        try:
            page_obj = paginator.page(current_page)
        except:
            page_obj = paginator.page(1)

        return render(
            request,
            'ProductsList',
            props={
                'products': [
                    {
                        'id': product.id,
                        'title': product.title,
                    }
                    for product in page_obj
                ],
                'pagination': {
                    'current_page': int(current_page),
                    'total_pages': page_obj.paginator.num_pages,
                    'has_prev': page_obj.has_previous(),
                    'has_next': page_obj.has_next(),
                    'prev_page': page_obj.previous_page_number() if page_obj.has_previous() else None,
                    'next_page': page_obj.next_page_number() if page_obj.has_next() else None,
                }
            }
        )

class ProductDetailView(DetailView):
    model = Product

    def get(self, request, *args, **kwargs):
        product = self.get_object()
        return render(
            request,
            'ProductDetail',
            props={
                'product': {
                    'title': product.title,
                    'description': product.description,
                }
            }
        )



class CreateProductView(View):
    def get(self, request):
        return render(request, 'CreateProduct')

    def post(self, request):
        title = request.POST.get('title', '').strip()
        description = request.POST.get('description', '').strip()

        Product.objects.create(
            title=title,
            description=description
        )

        return location('/products/') # ВАЖНО SPA РЕДИРЕКТ!

