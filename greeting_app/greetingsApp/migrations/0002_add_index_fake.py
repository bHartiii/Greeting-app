# Generated by Django 3.0.5 on 2020-12-19 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('greetingsApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='date',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
    ]
