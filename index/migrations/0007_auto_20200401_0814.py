# Generated by Django 3.0.4 on 2020-03-31 23:14

from django.db import migrations, models
import index.models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0006_auto_20200330_0541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='comment',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='information',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=index.models.user_portfolio_directory_path),
        ),
    ]
