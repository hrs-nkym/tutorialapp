from django.urls import path
from . import views

app_name = "app"

urlpatterns = [
    path("calendar/api/holiday/", views.HolidayList.as_view(), name="holiday_list"),
]
