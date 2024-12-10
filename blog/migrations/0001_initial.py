# Generated by Django 3.2.25 on 2024-12-10 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cursos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curso', models.CharField(max_length=100)),
                ('camada', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Entregables',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_entrega', models.CharField(max_length=100)),
                ('fecha_de_entrega', models.DateField()),
                ('entregado', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Estudiantes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_estudiante', models.CharField(max_length=100)),
                ('apellido_estudiante', models.CharField(max_length=100)),
                ('email_estudiante', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Profesores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_profe', models.CharField(max_length=100)),
                ('apellido_profe', models.CharField(max_length=100)),
                ('email_profe', models.EmailField(max_length=254)),
                ('profesion', models.CharField(max_length=100)),
            ],
        ),
    ]