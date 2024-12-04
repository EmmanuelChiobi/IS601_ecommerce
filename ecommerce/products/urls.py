from django.urls import path, include
import products.views as views

urlpatterns = [path('', views.home),
               path('/product/<int:pid>', views.product),
               path('/search', views.search),
               path('/cart', views.cart)]