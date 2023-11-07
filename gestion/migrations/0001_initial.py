# Generated by Django 3.2.23 on 2023-11-07 01:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AsignacionTarea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('observaciones', models.TextField()),
                ('fecha_asignacion', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenido', models.TextField()),
                ('fecha_de_comentario', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Etiqueta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('duracion_estimada', models.FloatField()),
                ('fecha_inicio', models.DateField(default=django.utils.timezone.now)),
                ('fecha_finalizacion', models.TimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('prioridad', models.IntegerField()),
                ('estado', models.CharField(choices=[('PE', 'Pendiente'), ('PR', 'Progreso'), ('Co', 'Completada')], max_length=2)),
                ('completada', models.BooleanField()),
                ('fecha_creacion', models.DateField(default=django.utils.timezone.now)),
                ('hora_vencimiento', models.TimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('correo_electronico', models.CharField(max_length=100, unique=True)),
                ('contraseña', models.CharField(max_length=50)),
                ('fecha_registro', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
