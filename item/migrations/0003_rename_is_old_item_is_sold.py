# Generated by Django 4.2.2 on 2023-07-03 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_alter_category_options_item'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='is_old',
            new_name='is_sold',
        ),
    ]
