# Generated by Django 4.2.5 on 2023-10-04 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificate_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='university_name',
            field=models.CharField(default='University Of Global Vilalge, Barishal', max_length=100),
        ),
    ]
