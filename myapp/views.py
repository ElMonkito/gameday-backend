from django.http import JsonResponse

from myapp.services import read_csv


def get_csv_data(request):
    data, status = read_csv()
    return JsonResponse(data, safe=False, status=status)