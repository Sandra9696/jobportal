# Generated by Django 2.2.7 on 2019-12-24 10:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0009_auto_20191224_1550'),
    ]

    operations = [
        migrations.RenameField(
            model_name='viewcl',
            old_name='candid',
            new_name='cand',
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='cmpreg',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Companyregistration'),
        ),
        migrations.AlterField(
            model_name='viewcl',
            name='cand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Candidatereg'),
        ),
    ]
