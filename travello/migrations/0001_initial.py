# Generated by Django 3.0.8 on 2020-07-29 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tourisam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('offer', models.BooleanField(default=False)),
                ('city_pic', models.ImageField(default='', upload_to='')),
            ],
        ),
    ]
