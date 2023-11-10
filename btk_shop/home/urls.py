from django.urls import path, include, re_path
from . import views
urlpatterns = [
    path("",
        include([
            path("", views.index, name="index"),
            ]),
        ),
]