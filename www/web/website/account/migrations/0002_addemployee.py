# Generated by Django 2.0.4 on 2018-07-09 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='addemployee',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('Address', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('dob', models.IntegerField(default=50)),
            ],
        ),
    ]