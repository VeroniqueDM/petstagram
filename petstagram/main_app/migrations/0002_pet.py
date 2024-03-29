# Generated by Django 4.0.3 on 2022-04-06 02:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('type', models.CharField(choices=[('CAT', 'CAT'), ('DOG', 'DOG'), ('BUNNY', 'BUNNY'), ('OTHER', 'OTHER'), ('PARROT', 'PARROT'), ('FISH', 'FISH')], max_length=6)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.profile')),
            ],
            options={
                'unique_together': {('user_profile', 'name')},
            },
        ),
    ]
