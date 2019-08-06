from django.urls import path
from mis import views

urlpatterns = [
    path('monitor/cpu/info/', views.get_cpu_info),
    path('monitor/tce/package/', views.get_tce_package),
]
