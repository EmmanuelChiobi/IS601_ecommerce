from django.urls import path, include
import cart.views as views

#Mapping URL Patterns to their respective view in 'views'py' file.
urlpatterns = [
    path('', views.cart),
    path('add/<int:id>', views.cart_add),
    path('delete/<int:id>', views.cart_delete)
]