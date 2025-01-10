# Generated by Django 5.1.3 on 2025-01-10 08:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("account", "0002_alter_accountroletype_roletype"),
        ("car", "0002_carcategory"),
    ]

    operations = [
        migrations.CreateModel(
            name="Cart",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("quantity", models.PositiveIntegerField(default=1)),
                (
                    "account",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="carts",
                        to="account.account",
                    ),
                ),
                (
                    "car",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="carts",
                        to="car.car",
                    ),
                ),
            ],
            options={
                "db_table": "cart",
            },
        ),
    ]