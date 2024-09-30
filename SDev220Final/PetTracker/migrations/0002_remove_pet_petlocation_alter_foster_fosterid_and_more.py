# Generated by Django 5.1.1 on 2024-09-26 21:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("PetTracker", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="pet",
            name="petLocation",
        ),
        migrations.AlterField(
            model_name="foster",
            name="fosterID",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="foster",
            name="fosterState",
            field=models.CharField(
                choices=[
                    ("al", "AL"),
                    ("ak", "AK"),
                    ("az", "AZ"),
                    ("ar", "AR"),
                    ("ca", "CA"),
                    ("co", "CO"),
                    ("ct", "CT"),
                    ("de", "DE"),
                    ("fl", "FL"),
                    ("ga", "GA"),
                    ("hi", "HI"),
                    ("id", "ID"),
                    ("il", "IL"),
                    ("in", "IN"),
                    ("ia", "IA"),
                    ("ks", "KS"),
                    ("ky", "KY"),
                    ("la", "LA"),
                    ("me", "ME"),
                    ("md", "MD"),
                    ("ma", "MA"),
                    ("mi", "MI"),
                    ("mn", "MN"),
                    ("ms", "MS"),
                    ("mo", "MO"),
                    ("mt", "MT"),
                    ("ne", "NE"),
                    ("nv", "NV"),
                    ("nh", "NH"),
                    ("nj", "NJ"),
                    ("nm", "NM"),
                    ("ny", "NY"),
                    ("nc", "NC"),
                    ("nd", "ND"),
                    ("oh", "OH"),
                    ("ok", "OK"),
                    ("or", "OR"),
                    ("pa", "PA"),
                    ("ri", "RI"),
                    ("sc", "SC"),
                    ("sd", "SD"),
                    ("tn", "TN"),
                    ("tx", "TX"),
                    ("ut", "UT"),
                    ("vt", "VT"),
                    ("va", "VA"),
                    ("wa", "WA"),
                    ("wv", "WV"),
                    ("wi", "WI"),
                    ("wy", "WY"),
                ],
                max_length=2,
            ),
        ),
        migrations.AlterField(
            model_name="organization",
            name="orgID",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="organization",
            name="orgState",
            field=models.CharField(
                choices=[
                    ("al", "AL"),
                    ("ak", "AK"),
                    ("az", "AZ"),
                    ("ar", "AR"),
                    ("ca", "CA"),
                    ("co", "CO"),
                    ("ct", "CT"),
                    ("de", "DE"),
                    ("fl", "FL"),
                    ("ga", "GA"),
                    ("hi", "HI"),
                    ("id", "ID"),
                    ("il", "IL"),
                    ("in", "IN"),
                    ("ia", "IA"),
                    ("ks", "KS"),
                    ("ky", "KY"),
                    ("la", "LA"),
                    ("me", "ME"),
                    ("md", "MD"),
                    ("ma", "MA"),
                    ("mi", "MI"),
                    ("mn", "MN"),
                    ("ms", "MS"),
                    ("mo", "MO"),
                    ("mt", "MT"),
                    ("ne", "NE"),
                    ("nv", "NV"),
                    ("nh", "NH"),
                    ("nj", "NJ"),
                    ("nm", "NM"),
                    ("ny", "NY"),
                    ("nc", "NC"),
                    ("nd", "ND"),
                    ("oh", "OH"),
                    ("ok", "OK"),
                    ("or", "OR"),
                    ("pa", "PA"),
                    ("ri", "RI"),
                    ("sc", "SC"),
                    ("sd", "SD"),
                    ("tn", "TN"),
                    ("tx", "TX"),
                    ("ut", "UT"),
                    ("vt", "VT"),
                    ("va", "VA"),
                    ("wa", "WA"),
                    ("wv", "WV"),
                    ("wi", "WI"),
                    ("wy", "WY"),
                ],
                max_length=2,
            ),
        ),
        migrations.AlterField(
            model_name="pet",
            name="petBio",
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name="pet",
            name="petDOB",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="pet",
            name="petFoster",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="PetTracker.foster",
            ),
        ),
        migrations.AlterField(
            model_name="pet",
            name="petID",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="pet",
            name="petImage",
            field=models.FileField(blank=True, null=True, upload_to=""),
        ),
        migrations.AlterField(
            model_name="pet",
            name="petMicrochipID",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="pet",
            name="petOrganization",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="PetTracker.organization",
            ),
        ),
        migrations.AlterField(
            model_name="pet",
            name="petRecords",
            field=models.FileField(blank=True, null=True, upload_to=""),
        ),
        migrations.AlterField(
            model_name="pet",
            name="petSex",
            field=models.CharField(
                choices=[
                    ("female", "Female"),
                    ("male", "Male"),
                    ("unknown", "Unknown"),
                ],
                max_length=10,
            ),
        ),
        migrations.AlterField(
            model_name="pet",
            name="petSpayNeuter",
            field=models.CharField(
                choices=[("no", "No"), ("yes", "Yes"), ("unknown", "Unknown")],
                max_length=10,
            ),
        ),
        migrations.AlterField(
            model_name="pet",
            name="petStatus",
            field=models.CharField(
                choices=[
                    ("available", "Available"),
                    ("notReady", "Not Ready Yet"),
                    ("adopted", "Already Adopted"),
                ],
                max_length=15,
            ),
        ),
        migrations.AlterField(
            model_name="pet",
            name="petType",
            field=models.CharField(
                choices=[("cat", "Cat"), ("dog", "Dog"), ("other", "Other")],
                max_length=10,
            ),
        ),
    ]