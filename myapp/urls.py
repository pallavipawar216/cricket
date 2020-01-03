"""cricket URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from . import views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('teams/', views.teams, name="teams"),
    path('teamhome/<team>', views.teamhome, name="teamhome"),
    path('ticketbook/<id>', views.ticketbook, name="ticketbook"),
    path('match_list/', views.match_list, name="match_list"),
    path("seat-query/", views.seat_query, name="seat_query"),
    path("check_seat/", views.check_seat, name="check_seat"),
    path('payment/', views.payment, name='payment'),
    path('booked_tickets/', views.booked_tickets, name='booked_tickets'),
]
