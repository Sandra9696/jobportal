# Generated by Django 2.2.7 on 2019-12-13 05:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20191212_1206'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidatereg',
            name='status',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='companyregistration',
            name='cmpstatus',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
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