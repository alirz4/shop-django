from django.shortcuts import render, get_object_or_404
from django.views import View

from product_module.models import Product, ProductGallery


class ProductList(View):
    data = Product.objects.filter(is_active=True)
    template_name = ''

    def get(self, request, *args, **kwargs):
        min_price = request.GET.get('min_price') or 0
        max_price = request.GET.get('max_price') or self.data.order_by('-price').first().price
        data = self.data.filter(price__lte=max_price, price__gte=min_price)
        return render(request, self.template_name, {'products': data})


class ProductDetail(View):
    template_name = ''

    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        gallery = ProductGallery.objects.filter(product_id=pk)
        return render(request, self.template_name, {'product': product,
                                                    'gallery': gallery})

