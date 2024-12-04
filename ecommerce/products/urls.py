from django.urls import path, include
import products.views as views

urlpatterns = [path('', views.home),
               path('/product/<int:id>', views.product),
               path('/search/<str:key>', views.search)]