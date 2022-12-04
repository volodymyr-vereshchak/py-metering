from django.shortcuts import render
from rest_framework import viewsets

from gas_meter_service.models import (
    Manufacturer,
    Size,
    City,
    Street,
    GasMeter,
    Contract,
    DailyTask,
    ReplacementAct,
)
from gas_meter_service.serializers import (
    ManufacturerSerializer,
    SizeSerializer,
    CitySerializer,
    StreetSerializer,
    GasMeterSerializer,
    ContractSerializer,
    DailyTaskSerializer,
    ReplacementActSerializer,
)



class ManufacturerView(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer


class SizeView(viewsets.ModelViewSet):
    queryset = Size.objects.all()
    serializer_class = SizeSerializer


class CityView(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class StreetView(viewsets.ModelViewSet):
    queryset = Street.objects.all()
    serializer_class = StreetSerializer


class GasMeterView(viewsets.ModelViewSet):
    queryset = GasMeter.objects.all()
    serializer_class = GasMeterSerializer


class ContractView(viewsets.ModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer


class DailyTaskView(viewsets.ModelViewSet):
    queryset = DailyTask.objects.all()
    serializer_class = DailyTaskSerializer


class ReplacementActView(viewsets.ModelViewSet):
    queryset = ReplacementAct.objects.all()
    serializer_class = ReplacementActSerializer
