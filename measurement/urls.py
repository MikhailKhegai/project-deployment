from django.urls import path
from measurement.views import SensorCreateView, SensorUpdate, MeasurmentsCreateView


urlpatterns = [
    path('sensors/', SensorCreateView.as_view()),
    path('sensors/<int:pk>/', SensorUpdate.as_view()),
    path('measurements/', MeasurmentsCreateView.as_view()),
]
