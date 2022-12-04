from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError


class Manufacturer(models.Model):
    name = models.CharField(max_length=32)


class Size(models.Model):
    name = models.CharField(max_length=16)
    max_flow = models.PositiveIntegerField()
    min_flow = models.PositiveIntegerField()


class City(models.Model):
    name = models.CharField(max_length=64)


class Street(models.Model):
    name = models.CharField(max_length=64)
    city = models.ForeignKey(City, on_delete=models.CASCADE)


class GasMeter(models.Model):
    name = models.CharField(max_length=32)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    serial_number = models.CharField(max_length=12)
    date_of_prodaction = models.DateField()
    date_of_next_verification = models.DateField()
    date_of_installation = models.DateField()
    meter_reading = models.PositiveIntegerField()


class Contract(models.Model):
    personal_account = models.CharField(max_length=12, blank=True, null=True)
    subscriber = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    street = models.ForeignKey(Street, on_delete=models.CASCADE)
    hous = models.PositiveIntegerField()
    apartment = models.PositiveIntegerField(blank=True, null=True)
    gas_meters = models.ManyToManyField(GasMeter, blank=True)


class DailyTask(models.Model):
    day_of_task = models.DateField(auto_now_add=True)
    locksmith = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    contracts = models.ManyToManyField(Contract)
    gas_meters = models.ManyToManyField(GasMeter, blank=True)
    
    @staticmethod
    def validate_dailytask(day_of_task: str, contracts: list[int]) -> None:
        for contract in contracts:
            query_set = Contract.objects.filter(id=contract).values("gas_meters__day_of_next_verification", "perosnal_account")
            if day_of_task < query_set["day_of_next_verification"]:
                raise ValidationError(f"{query_set['perosnal_account']}: day of next verification must be less then day of task!")

    def clean(self) -> None:
        self.validate_dailytask(self.day_of_task, self.contracts)


class ReplacementAct(models.Model):
    day_of_act = models.DateField(auto_now_add=True)
    daily_task = models.ForeignKey(DailyTask, on_delete=models.CASCADE)
    gas_meter_remove = models.ForeignKey(GasMeter, on_delete=models.CASCADE, related_name="meter_remove")
    remove_meter_reading = models.PositiveIntegerField()
    gas_meter_installable = models.ForeignKey(GasMeter, on_delete=models.CASCADE, related_name="meter_install")
    installable_meter_reading = models.PositiveIntegerField()
