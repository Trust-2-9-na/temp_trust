
from django.urls import path 
from temp.views import index, SensorDataList

urlpatterns = [
  path('', index, name='index'),  # The index view that renders sensor data in HTML
  path('api/sensor-data/', SensorDataList.as_view(), name='sensor-data-list'), 
]