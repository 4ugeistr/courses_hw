# Generated by Django 3.2.13 on 2022-06-17 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_auto_20220617_1653'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentgroup',
            name='students_number',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=4, null=True, verbose_name='Кол-во студентов'),
        ),
    ]