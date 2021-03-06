# Generated by Django 2.2.7 on 2019-12-11 04:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('category', models.CharField(max_length=20)),
                ('status', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='companyregistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cmpname', models.CharField(max_length=20)),
                ('cmpemail', models.CharField(max_length=20)),
                ('cmpmobile', models.CharField(max_length=10)),
                ('cmpaddress', models.CharField(max_length=50)),
                ('cmpstate', models.CharField(max_length=10)),
                ('cmpdescription', models.CharField(max_length=10)),
                ('cmpusername', models.CharField(max_length=20)),
                ('cmppassword', models.CharField(max_length=20)),
                ('cmpregisterid', models.CharField(max_length=20)),
                ('cmpowner', models.CharField(max_length=20)),
                ('cmplogin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.login')),
            ],
        ),
        migrations.CreateModel(
            name='candidatereg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('address', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=10)),
                ('mobile', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('qualification', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=10)),
                ('skills', models.CharField(max_length=20)),
                ('resume', models.FileField(upload_to='fileup')),
                ('canlogin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.login')),
            ],
        ),
    ]
