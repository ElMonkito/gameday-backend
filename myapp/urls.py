from django.urls import path
from myapp.views import get_csv_data
from myapp.views import run_csv_downloader

urlpatterns = [
    path('data/', get_csv_data, name='get_csv_data'),
    path('run-script/', run_csv_downloader, name='run_csv_downloader'),
]