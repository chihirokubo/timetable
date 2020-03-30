# Generated by Django 3.0.4 on 2020-03-29 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_auto_20200330_0444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='comment',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='information',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='myclass',
            name='day',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='myclass',
            name='period',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='myclass',
            name='place',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
