# Generated by Django 5.1.1 on 2024-09-29 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("PetTracker", "0003_foster_orgphone_organization_orgphone"),
    ]

    operations = [
        migrations.AlterField(
            model_name="foster",
            name="orgPhone",
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name="organization",
            name="orgPhone",
            field=models.CharField(max_length=10, null=True),
        ),
    ]