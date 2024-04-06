from django.urls import path
from .views import RunListCreateView, RunDetailView

urlpatterns = [
    path("", RunListCreateView.as_view(), name="run-list-create"),
    path("<int:pk>/", RunDetailView.as_view(), name="run-detail"),
]
