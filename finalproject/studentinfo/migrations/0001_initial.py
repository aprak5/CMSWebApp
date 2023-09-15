# Generated by Django 4.2 on 2023-04-27 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentInfo',
            fields=[
                ('studentid', models.IntegerField(primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('studentmajor', models.CharField(max_length=100)),
                ('studentyear', models.CharField(max_length=100)),
                ('gpa', models.DecimalField(decimal_places=1, max_digits=2)),
            ],
        )
    ]