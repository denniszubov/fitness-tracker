from django.urls import include, path

urlpatterns = [
    path("run/", include("run.urls")),
]
