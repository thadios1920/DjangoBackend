from django.urls import path
from . import views


urlpatterns = [
    path('',views.getRoutes,name='routes'),
    path('products',views.getProducts,name='produits'),
    path('products/<str:pk>',views.getProduct,name='produit')
]