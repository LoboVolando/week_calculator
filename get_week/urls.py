from django.urls import path
from get_week.views import *


app_name = 'get_week'

urlpatterns = [
    path('', DateView.as_view(), name='main'),
    path('api/', api_date_view, name='account-payment'),
]
