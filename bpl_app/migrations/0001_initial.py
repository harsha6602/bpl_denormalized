# Generated by Django 4.2.1 on 2023-08-16 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Matches",
            fields=[
                (
                    "match_no",
                    models.CharField(
                        max_length=12, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("team1_id", models.CharField(max_length=128, unique=True)),
                ("team2_id", models.CharField(max_length=128, unique=True)),
                ("umpire_name", models.CharField(default="none", max_length=128)),
                ("runs", models.IntegerField(default=0)),
                ("wickets", models.IntegerField(default=0)),
                ("status", models.CharField(max_length=128)),
                ("overs", models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name="TeamsInfo",
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
                ("team_id", models.CharField(max_length=128, unique=True)),
                ("player_id", models.CharField(max_length=12, unique=True)),
                ("team_name", models.CharField(max_length=128, unique=True)),
                ("captain_phoneno", models.CharField(max_length=12)),
                ("player_role", models.CharField(max_length=128, null=True)),
                ("phone_no", models.CharField(max_length=12, unique=True)),
                ("branch", models.CharField(max_length=128)),
                ("player_name", models.CharField(max_length=128, null=True)),
                ("sport", models.CharField(default="null", max_length=12)),
            ],
        ),
    ]