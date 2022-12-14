# Generated by Django 4.1.3 on 2022-12-04 15:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("gas_meter_service", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="dailytask",
            name="locksmith",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="contract",
            name="gas_meters",
            field=models.ManyToManyField(blank=True, to="gas_meter_service.gasmeter"),
        ),
        migrations.AddField(
            model_name="contract",
            name="street",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="gas_meter_service.street",
            ),
        ),
        migrations.AddField(
            model_name="contract",
            name="subscriber",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
