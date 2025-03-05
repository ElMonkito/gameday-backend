from django.urls import path
from myapp.views import get_csv_data

urlpatterns = [
    path('data/', get_csv_data, name='get_csv_data'),
]