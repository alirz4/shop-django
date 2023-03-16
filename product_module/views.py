from django.shortcuts import render, get_object_or_404
from django.views import View

from product_module.models import Product


class ProductList(View):
    data = Product.objects.filter(is_active=True)
    template_name = ''

    def get(self, request):
        return render(request, self.template_name, {'products': self.data})


class ProductDetail(View):
    template_name = ''

    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        return render(request, self.template_name, {'product': product})
