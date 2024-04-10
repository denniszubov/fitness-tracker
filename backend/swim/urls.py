from django.urls import path
from .views import SwimListCreateView, SwimDetailView

urlpatterns = [
    path("", SwimListCreateView.as_view(), name="swim-list-create"),
    path("<int:pk>/", SwimDetailView.as_view(), name="swim-detail"),
]
