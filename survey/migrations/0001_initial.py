# Generated by Django 3.0.3 on 2020-02-15 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('skills', models.CharField(max_length=80)),
                ('city', models.CharField(max_length=80)),
                ('age', models.IntegerField()),
                ('edc_background', models.TextField()),
            ],
        ),
    ]
