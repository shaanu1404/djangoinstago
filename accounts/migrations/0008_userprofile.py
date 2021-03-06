# Generated by Django 3.0.7 on 2020-06-26 07:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0007_delete_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, null=True)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='images/profile-image/%Y/%m/%d/')),
                ('following', models.ManyToManyField(blank=True, related_name='_userprofile_following_+', to='accounts.UserProfile')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
