# Generated by Django 3.0.3 on 2020-03-22 23:24

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=60)),
                ('description', models.TextField(default='', max_length=1000)),
                ('init_date', models.DateTimeField(default=datetime.datetime.now)),
                ('end_date', models.DateTimeField(blank=True, default=None, null=True)),
                ('status', models.CharField(choices=[('New', 'New'), ('In progress', 'Inprogress'), ('Waiting', 'Waiting'), ('Closed', 'Closed')], default='New', max_length=60)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Vacation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('init_date', models.DateTimeField(blank=True, default=None, null=True)),
                ('end_date', models.DateTimeField(blank=True, default=None, null=True)),
                ('description', models.TextField(default='', max_length=1000)),
                ('aproved', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(choices=[('RS', 'Estudiante por requerimientos'), ('PS', 'Estudiante fijo'), ('TR', 'Trainee'), ('JR', 'Junior'), ('SS', 'Semi-Senior'), ('SR', 'Senior')], default='RS', max_length=60)),
                ('remaining_vac_days', models.IntegerField(default=30)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TimeInterval',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('init_time', models.DateTimeField(default=datetime.datetime.now)),
                ('end_time', models.DateTimeField(blank=True, default=None, null=True)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Task')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True, default=None, null=True)),
                ('description', models.TextField(default='', max_length=1000)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Advancement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=30)),
                ('description', models.TextField(default='', max_length=1000)),
                ('aproved', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
