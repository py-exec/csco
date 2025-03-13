from django.urls import path
from .views import CartonFormView, add_customer_ajax, get_customers_ajax, CartonOrderListView

urlpatterns = [

    path('CartonOrdernew/', CartonFormView.as_view(), name='new_order'),
    path('ordersView/', CartonOrderListView.as_view(), name='carton_order_list'),
    path('add-customer/', add_customer_ajax, name='add_customer_ajax'),  # مسیر اضافه شد
    path("get-customers/", get_customers_ajax, name="get_customers_ajax"),

]
