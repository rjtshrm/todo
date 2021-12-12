import time
from django.http import JsonResponse
import os

# Create your views here.
def get(request):
    return JsonResponse({
        "Get": 'successfully received'
    })



def put(request):
    return JsonResponse({
        "Put": 'successfully received'
    })


def delete(request):
    return JsonResponse({
        "Delete": 'successfully received'
    })

def create_temp_file(request):
    os.system(f"echo {time.time()} >> /mnt/web_data/log.txt")

def consume_cpu(request):
    os.system("stress-ng -c 0 -l 80")

    return JsonResponse({
        "Consume cpu": 'successfully received'
    })