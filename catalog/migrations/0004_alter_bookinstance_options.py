# Generated by Django 3.2.4 on 2021-06-22 10:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_bookinstance_borrower'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinstance',
            options={'ordering': ['due_back'], 'permissions': (('can_mark_returned', 'Set book as returned'),)},
        ),
    ]
