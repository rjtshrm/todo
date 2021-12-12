from django.urls import include, path
from . import views

urs_patterns = [
    path("get/", views.get, name="GET"),
    path("put/", views.put, name="PUT"),
    path("delete/", views.delete, name="DELETE"),
    path("create_temp_file/", views.create_temp_file, name="CREATE_TEMP_FILE"),
    path("consume_cpu/", views.consume_cpu, name="CONSUME_CPU"),
]