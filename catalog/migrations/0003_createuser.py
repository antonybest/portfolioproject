# Generated by Django 3.1.3 on 2020-12-09 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20201209_1114'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreateUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=200)),
                ('date_of_birth', models.DateField()),
            ],
        ),
    ]
