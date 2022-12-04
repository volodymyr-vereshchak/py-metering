from rest_framework import serializers

from gas_meter_service.models import (
    Manufacturer, 
    Size, 
    City, 
    Street,
    GasMeter,
    Contract,
    DailyTask,
    ReplacementAct
)


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = "__all__"


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = "__all__"


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = "__all__"


class StreetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Street
        fields = "__all__"


class GasMeterSerializer(serializers.ModelSerializer):
    class Meta:
        model = GasMeter
        fields = "__all__"


class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = "__all__"


class DailyTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyTask
        fields = "__all__"


class ReplacementActSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReplacementAct
        fields = "__all__"
