# Generated by Django 3.1.3 on 2020-11-02 16:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='region',
            old_name='champions',
            new_name='champions_count',
        ),
    ]