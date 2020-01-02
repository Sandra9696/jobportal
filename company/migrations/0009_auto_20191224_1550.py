# Generated by Django 2.2.7 on 2019-12-24 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_auto_20191224_1550'),
        ('company', '0008_auto_20191224_1424'),
    ]

    operations = [
        migrations.AddField(
            model_name='viewcl',
            name='candid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Candidatereg'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='viewcl',
            name='vacan',
            field=models.CharField(default=0, max_length=5),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='cmpreg',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Companyregistration'),
        ),
    ]
