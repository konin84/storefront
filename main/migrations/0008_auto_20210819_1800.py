# Generated by Django 3.2.6 on 2021-08-19 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_testing'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactus',
            old_name='content',
            new_name='message',
        ),
        migrations.AddField(
            model_name='contactus',
            name='subject',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
