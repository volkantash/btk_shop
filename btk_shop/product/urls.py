from django.urls import path, include
from . import views

değişken = 'product/'

urlpatterns = [
    path(değişken,
        include([
            path("", views.index, name="index"),
            path("<slug:url>/", views.index, name="index"),
            ]),
        ),
]