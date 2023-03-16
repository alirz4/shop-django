from django.urls import path
from . import views

app_name = 'product_module'

urlpatterns = [
    path('', views.ProductList.as_view(), name='prod_list'),
    path('detail/<int:pk>/', views.ProductDetail.as_view(), name='prod_detail'),
]