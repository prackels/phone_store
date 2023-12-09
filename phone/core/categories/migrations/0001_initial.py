# Generated by Django 4.2.7 on 2023-12-03 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=30)),
                ('processor', models.CharField(max_length=30)),
                ('ram', models.IntegerField()),
                ('storage', models.IntegerField()),
            ],
        ),
    ]