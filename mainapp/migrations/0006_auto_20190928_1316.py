# Generated by Django 2.2.3 on 2019-09-28 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_auto_20190928_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comingrequests',
            name='command_name',
            field=models.CharField(max_length=32, verbose_name='название команды'),
        ),
    ]
