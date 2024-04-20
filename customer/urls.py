from customer.apps import CustomerConfig
from django.urls import path
from customer.views import CustomerListView, CustomerCreateView, CustomerUpdateView, CustomerDetailView, CustomerDeleteView

app_name = CustomerConfig.name


urlpatterns = [
    path("", CustomerListView.as_view(), name="all_customers"),
    path("add_customer/", CustomerCreateView.as_view(), name="add_customer"),
    path('customer_update/<int:pk>', CustomerUpdateView.as_view(), name='customer_update'),
    path("customer_details/<int:pk>", CustomerDetailView.as_view(), name="customer_details"),
    path("delete_customer/<int:pk>", CustomerDeleteView.as_view(), name="delete_customer"),
]
