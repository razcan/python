# Generated by Django 3.1.4 on 2020-12-04 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distance', models.CharField(max_length=200)),
                ('time', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
