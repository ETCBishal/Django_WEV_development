# Generated by Django 4.0.3 on 2023-01-17 08:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_contact_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='description',
            new_name='desc',
        ),
    ]
