# Generated by Django 4.1 on 2022-08-05 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('artist', models.CharField(max_length=300)),
                ('album', models.CharField(max_length=300)),
                ('release_date', models.DateField()),
                ('genre', models.CharField(max_length=300)),
            ],
        ),
    ]
