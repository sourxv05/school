# Generated by Django 4.2.6 on 2023-10-21 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sapp', '0003_alter_course_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=200),
        ),
    ]
