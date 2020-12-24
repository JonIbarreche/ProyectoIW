# Generated by Django 3.1.1 on 2020-11-17 07:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20201021_1123'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estilo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Interprete',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('DNI', models.CharField(max_length=9)),
                ('fecha', models.DateField()),
                ('descripcion', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Cancion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=30)),
                ('fecha', models.DateField()),
                ('link', models.CharField(max_length=300)),
                ('estilo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.estilo')),
                ('interprete', models.ManyToManyField(to='myapp.Interprete')),
            ],
        ),
    ]