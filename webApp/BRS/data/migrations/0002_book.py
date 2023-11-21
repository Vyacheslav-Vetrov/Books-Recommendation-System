# Generated by Django 4.2.6 on 2023-11-21 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn', models.IntegerField(verbose_name='ISBN')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('status', models.CharField(max_length=200, verbose_name='Status')),
                ('genre', models.CharField(max_length=100, verbose_name='Genre')),
            ],
        ),
    ]
