from django.urls import path

from . import views

urlpatterns = [
    path("", views.index), # /challenges/
    path("<int:month>", views.monthly_challenge_by_number), # filter usreinput `<int:month>` just int
    path("<str:month>", views.monthly_challenge, name="month-challenge") # filter usreinput `<str:month>` just str
]
