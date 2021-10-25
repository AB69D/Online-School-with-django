# Generated by Django 2.2.10 on 2021-05-11 06:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0025_auto_20201012_0955'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkingDays',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TimeSlots',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('standard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='time_slots', to='curriculum.Standard')),
            ],
        ),
    ]