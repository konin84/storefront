# Generated by Django 3.2.6 on 2021-08-12 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210812_1535'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyinfo',
            name='image',
            field=models.ImageField(null=True, upload_to='company/photo'),
        ),
    ]
