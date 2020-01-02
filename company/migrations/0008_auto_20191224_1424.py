# Generated by Django 2.2.7 on 2019-12-24 08:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0007_auto_20191223_1133'),
    ]

    operations = [
        migrations.CreateModel(
            name='Viewcl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=20)),
                ('message', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='cmpreg',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Companyregistration'),
        ),
    ]
