# Generated by Django 2.2.7 on 2019-12-23 05:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0005_auto_20191218_1228'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vacancy',
            old_name='keyskills',
            new_name='skills',
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='cmpreg',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Companyregistration'),
        ),
    ]
