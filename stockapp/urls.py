from rest_framework.routers import DefaultRouter

from django.urls import path, include
from stockapp.views import KospiData, ChartView, KospiViewSet, KospiCreate, KospiDelete

app_name = "stockapp"

router = DefaultRouter()
router.register(r'post/', KospiViewSet)

urlpatterns = [
    path('api/',include(router.urls)),
    path('chart/', ChartView.as_view(), name="chart"),
    path('data/', KospiData),
    path('create/', KospiCreate, name="create"),
    path('delete/<int:pk>', KospiDelete, name="delete"),
]