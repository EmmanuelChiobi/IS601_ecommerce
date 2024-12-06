from django.urls import path, include
import products.views as views

#Mapping URL Patterns to their respective view in 'views'py' file.
urlpatterns = [path('', views.home),
               path('product/<int:pid>', views.product),
               path('search', views.search),
               ]