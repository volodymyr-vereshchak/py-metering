# Generated by Django 4.1.3 on 2022-12-04 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="City",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name="Contract",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "personal_account",
                    models.CharField(blank=True, max_length=12, null=True),
                ),
                ("hous", models.PositiveIntegerField()),
                ("apartment", models.PositiveIntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="DailyTask",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("day_of_task", models.DateField(auto_now_add=True)),
                ("contracts", models.ManyToManyField(to="gas_meter_service.contract")),
            ],
        ),
        migrations.CreateModel(
            name="GasMeter",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=32)),
                ("serial_number", models.CharField(max_length=12)),
                ("date_of_prodaction", models.DateField()),
                ("date_of_verification", models.DateField()),
                ("date_of_installation", models.DateField()),
                ("meter_reading", models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Manufacturer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name="Size",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=16)),
                ("max_flow", models.PositiveIntegerField()),
                ("min_flow", models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Street",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=64)),
                (
                    "city",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="gas_meter_service.city",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ReplacementAct",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("day_of_act", models.DateField(auto_now_add=True)),
                ("remove_meter_reading", models.PositiveIntegerField()),
                ("installable_meter_reading", models.PositiveIntegerField()),
                (
                    "daily_task",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="gas_meter_service.dailytask",
                    ),
                ),
                (
                    "gas_meter_installable",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="meter_install",
                        to="gas_meter_service.gasmeter",
                    ),
                ),
                (
                    "gas_meter_remove",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="meter_remove",
                        to="gas_meter_service.gasmeter",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="gasmeter",
            name="manufacturer",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="gas_meter_service.manufacturer",
            ),
        ),
        migrations.AddField(
            model_name="gasmeter",
            name="size",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="gas_meter_service.size"
            ),
        ),
        migrations.AddField(
            model_name="dailytask",
            name="gas_meters",
            field=models.ManyToManyField(blank=True, to="gas_meter_service.gasmeter"),
        ),
    ]
