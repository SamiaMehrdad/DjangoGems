# Generated by Django 3.1.4 on 2020-12-14 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_famous'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='famous',
            name='Ownership',
        ),
        migrations.AddField(
            model_name='famous',
            name='ownership',
            field=models.CharField(choices=[('P', 'Private'), ('R', 'Royal'), ('M', 'Museum')], default='P', max_length=1, verbose_name='Type of ownership'),
        ),
    ]