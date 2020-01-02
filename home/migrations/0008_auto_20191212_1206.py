# Generated by Django 2.2.7 on 2019-12-12 06:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20191212_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidatereg',
            name='canlogin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Login'),
        ),
        migrations.AlterField(
            model_name='companyregistration',
            name='cmpemail',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='companyregistration',
            name='cmplogin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Login'),
        ),
    ]
