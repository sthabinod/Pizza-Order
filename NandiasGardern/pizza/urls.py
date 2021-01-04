from django.urls import path
from . import views
from .views import ListPizza, pizzas

urlpatterns = [
   path('',views.index,name='index'),
   path('order/',views.order,name='order'),
   path('view-pizza/',ListPizza.as_view(),name='list_pizza'),
   path('pizzas/',views.pizzas,name='pizzas'),
   path('pizzas/<int:id>',views.edit_order,name='pizzas_edit'),
   path('rules/',views.rules, name='rules')
]