# Generated by Django 3.1.7 on 2021-03-25 20:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ViewerProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics', verbose_name='Profile picture')),
                ('city', models.CharField(max_length=100, verbose_name='City')),
                ('state', models.CharField(max_length=100, verbose_name='State')),
                ('doj', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date of Joining')),
                ('dob', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date of Birth')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='vprofile', to=settings.AUTH_USER_MODEL, verbose_name='username')),
            ],
        ),
        migrations.CreateModel(
            name='CreatorProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics', verbose_name='Profile picture')),
                ('city', models.CharField(max_length=100, verbose_name='City')),
                ('state', models.CharField(max_length=100, verbose_name='State')),
                ('doj', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date of Joining')),
                ('dob', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date of Birth')),
                ('edu', models.TextField(verbose_name='Education Qualification')),
                ('rating', models.DecimalField(decimal_places=2, default=0, max_digits=3)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='cprofile', to=settings.AUTH_USER_MODEL, verbose_name='username')),
            ],
        ),
    ]
