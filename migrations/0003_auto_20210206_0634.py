# Generated by Django 2.2 on 2021-02-06 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LoanApp', '0002_userdetails_allot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='Allot',
            field=models.IntegerField(default=100000),
        ),
    ]