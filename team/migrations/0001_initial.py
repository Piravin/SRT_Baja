# Generated by Django 3.0.7 on 2020-08-18 05:11

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='#', max_length=100)),
                ('carpic', models.ImageField(blank=True, default='default.png', upload_to='Cars')),
            ],
        ),
        migrations.CreateModel(
            name='Subsystem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=20)),
                ('photo', models.ImageField(default='default.jpg', upload_to='Teams')),
            ],
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('photo', models.ImageField(default='default.png', upload_to='Team_profile_pics')),
                ('role', models.CharField(blank=True, default='member', max_length=100)),
                ('year_of_study', models.CharField(max_length=1)),
                ('linked_in', models.CharField(default='#', max_length=1000)),
                ('description', models.TextField()),
                ('subsystem', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='team.Subsystem')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team.Team')),
            ],
        ),
        migrations.CreateModel(
            name='CarDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(blank=True, max_length=100)),
                ('description', ckeditor.fields.RichTextField(blank=True)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team.Car')),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team.Team'),
        ),
    ]
