from performer.apps import PerformerConfig
from django.urls import path
from performer.views import PerformerListView, PerformerCreateView, PerformerUpdateView, PerformerDetailView, PerformerDeleteView

app_name = PerformerConfig.name


urlpatterns = [
    path("all_performers/", PerformerListView.as_view(), name="all_performers"),
    path("add_performer/", PerformerCreateView.as_view(), name="add_performer"),
    path('performer_update/<int:pk>', PerformerUpdateView.as_view(), name='performer_update'),
    path("performer_details/<int:pk>", PerformerDetailView.as_view(), name="performer_details"),
    path("delete_performer/<int:pk>", PerformerDeleteView.as_view(), name="delete_performer"),
]
