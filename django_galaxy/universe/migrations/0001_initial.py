# Generated by Django 4.0.3 on 2023-12-24 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Blackhole', '0003_blackhole_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Galaxy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('size', models.IntegerField()),
                ('dark_matter', models.BooleanField()),
                ('star_count', models.IntegerField()),
                ('Collision_time', models.IntegerField()),
                ('center', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Blackhole.blackhole')),
            ],
        ),
        migrations.CreateModel(
            name='Universe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='SolarSystem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('number_of_planets', models.IntegerField()),
                ('number_of_stars', models.IntegerField()),
                ('galaxy_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='universe.galaxy')),
            ],
        ),
        migrations.CreateModel(
            name='Planet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('size', models.IntegerField()),
                ('habitable', models.BooleanField()),
                ('lowest_temperature', models.IntegerField()),
                ('highest_temperature', models.IntegerField()),
                ('gravity', models.IntegerField()),
                ('solar_system', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='universe.solarsystem')),
            ],
        ),
        migrations.AddField(
            model_name='galaxy',
            name='universe_name',
            field=models.ManyToManyField(to='universe.universe'),
        ),
    ]
