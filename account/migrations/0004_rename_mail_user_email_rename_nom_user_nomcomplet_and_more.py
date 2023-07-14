# Generated by Django 4.1.7 on 2023-05-12 19:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_remove_user_pseudo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='mail',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='nom',
            new_name='nomComplet',
        ),
        migrations.RemoveField(
            model_name='user',
            name='niveau',
        ),
        migrations.RemoveField(
            model_name='user',
            name='prenom',
        ),
    ]