# Generated by Django 3.2.2 on 2021-05-20 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("warehouse", "0013_auto_20210308_1135"),
    ]

    operations = [
        migrations.AddField(
            model_name="warehouse",
            name="click_and_collect_option",
            field=models.CharField(
                choices=[
                    ("disabled", "Disabled"),
                    ("local", "Local stock only"),
                    ("all", "All warehouses"),
                ],
                default="disabled",
                max_length=30,
            ),
        ),
        migrations.AddField(
            model_name="warehouse",
            name="is_private",
            field=models.BooleanField(default=True),
        ),
    ]
