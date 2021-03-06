# Generated by Django 3.2.6 on 2021-08-11 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DrugsReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('condition', models.CharField(default='', max_length=255)),
                ('date', models.DateField(null=True)),
                ('drug_name', models.CharField(default='', max_length=255)),
                ('rating', models.CharField(default='', max_length=255)),
                ('review', models.CharField(default='', max_length=255)),
                ('useful_count', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PharmaSales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=255)),
                ('datum', models.DateTimeField(auto_now_add=True)),
                ('m01ab', models.CharField(max_length=255)),
                ('m01ae', models.CharField(max_length=255)),
                ('n02ba', models.CharField(max_length=255)),
                ('n02be', models.CharField(max_length=255)),
                ('n05b', models.CharField(max_length=255)),
                ('n05c', models.CharField(max_length=255)),
                ('r03', models.CharField(max_length=255)),
                ('r06', models.CharField(max_length=255)),
            ],
        ),
    ]
