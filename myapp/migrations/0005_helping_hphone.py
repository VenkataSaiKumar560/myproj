# Generated by Django 3.1.1 on 2020-12-16 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_helping'),
    ]

    operations = [
        migrations.AddField(
            model_name='helping',
            name='Hphone',
            field=models.CharField(max_length=10, null=True),
        ),
    ]