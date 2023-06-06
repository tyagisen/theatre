from django.urls import path
from . import views


urlpatterns= [
    path('', views.SeatForPeople.as_view(), name="seat"),
]