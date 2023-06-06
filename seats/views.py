from django.shortcuts import render
from django.views.generic.list import ListView
from .models import CustomerSeat
# Create your views here.
class SeatForPeople(ListView):
    model = CustomerSeat
    template_name = "seats/seat.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["seats_data"] = "No thing"