from django.urls import path
from .views import RunListCreateView #, RunRetrieveUpdateDestroyView

urlpatterns = [
    path("", RunListCreateView.as_view(), name="run-list-create"),
]
