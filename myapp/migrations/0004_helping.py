# Generated by Django 3.1.1 on 2020-12-16 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20201216_1628'),
    ]

    operations = [
        migrations.CreateModel(
            name='Helping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hitem', models.CharField(max_length=30)),
                ('Hquantity', models.CharField(max_length=10)),
            ],
        ),
    ]
