# Generated by Django 2.2.7 on 2019-12-18 01:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20191213_1044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidatereg',
            name='canlogin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Login'),
        ),
        migrations.AlterField(
            model_name='companyregistration',
            name='cmplogin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Login'),
        ),
    ]
