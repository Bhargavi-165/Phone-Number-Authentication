# Generated by Django 5.0.6 on 2024-09-06 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_alter_register_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_data',
            fields=[
                ('fullname', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('phone', models.IntegerField()),
                ('msg', models.CharField(max_length=200)),
            ],
        ),
    ]
