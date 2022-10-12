from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('products/', views.get_products, name='products'),
    path('category/<slug:url>/', views.get_category, name='category'),
    path('product/<slug:url>/<int:pk>/', views.detail_product, name='detail_product'),

]
