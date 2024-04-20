from django.urls import path

from customer.apps import CustomerConfig
from customer.views import (
    CustomerCreateView,
    CustomerDeleteView,
    CustomerDetailView,
    CustomerListView,
    CustomerUpdateView,
)

app_name = CustomerConfig.name


urlpatterns = [
    path("all_customers/", CustomerListView.as_view(), name="all_customers"),
    path("add_customer/", CustomerCreateView.as_view(), name="add_customer"),
    path(
        "customer_update/<int:pk>", CustomerUpdateView.as_view(), name="customer_update"
    ),
    path(
        "customer_details/<int:pk>",
        CustomerDetailView.as_view(),
        name="customer_details",
    ),
    path(
        "delete_customer/<int:pk>", CustomerDeleteView.as_view(), name="delete_customer"
    ),
]
