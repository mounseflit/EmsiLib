# Generated by Django 4.1.7 on 2023-04-18 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Livre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('auteur', models.CharField(max_length=100)),
                ('categorie', models.CharField(choices=[('Informatique', 'Informatique'), ('Automatisme', 'Automatisme'), ('Industriel', 'Industriel')], max_length=100)),
                ('etat', models.CharField(choices=[('Disponible', 'Disponible'), ('Réservé', 'Réservé'), ('Emprunté', 'Emprunté')], max_length=100)),
            ],
        ),
    ]
