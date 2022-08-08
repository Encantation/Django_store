# Generated by Django 4.0.6 on 2022-08-08 05:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hardware', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='goods',
            name='photo',
            field=models.ImageField(blank=True, upload_to='media/photos'),
        ),
    ]