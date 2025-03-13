import subprocess

from django.http import JsonResponse

from myapp.services import read_csv



def get_csv_data(request):
    data, status = read_csv()
    return JsonResponse(data, safe=False, status=status)

def run_csv_downloader(request):
    try:
        subprocess.run(["python3", "myapp/services/csv_downloader.py"], check=True)
        return JsonResponse({"message": "CSV downloader started"}, status=200)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)