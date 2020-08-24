from django.urls import path
from . import views as home_views

urlpatterns=[
    path('', home_views.homePage, name = "homepage"),
    path('cars',home_views.carsPage, name="carspage"),
    path('car/<str:pk>',home_views.carDetail, name="cardetail"),
    path('team',home_views.teamPage,name="teampage")
]