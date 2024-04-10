from django.urls import path
from customer import views

urlpatterns = [
    path('',views.customer_form , name='customer_form'),
    path('list/',views.customer_list , name='customer_list'),
    path('<int:id>/',views.customer_form , name='customer_update'),
    path('delete/<int:id>',views.customer_delete , name='customer_delete'),
]

