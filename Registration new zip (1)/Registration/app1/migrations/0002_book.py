# Generated by Django 4.1.3 on 2022-12-06 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imag', models.CharField(max_length=100)),
                ('capt', models.CharField(max_length=300)),
            ],
        ),
    ]
