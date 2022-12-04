from django.urls import path, include
from rest_framework import routers

from gas_meter_service.views import (
    ManufacturerView,
    SizeView,
    CityView,
    StreetView,
    GasMeterView,
    ContractView,
    DailyTaskView,
    ReplacementActView,
)

router = routers.DefaultRouter()
router.register("manufacturers", ManufacturerView)
router.register("sizes", SizeView)
router.register("cities", CityView)
router.register("streets", StreetView)
router.register("meters", GasMeterView)
router.register("contracts", ContractView)
router.register("tasks", DailyTaskView)
router.register("acts", ReplacementActView)

urlpatterns = [
    path("", include(router.urls))
]

app_name = "metering"
