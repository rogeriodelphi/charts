# Generated by Django 2.2.7 on 2020-02-18 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curso', models.CharField(max_length=60)),
                ('quantidade', models.CharField(max_length=3)),
                ('mes', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'Curso',
                'ordering': ['curso'],
            },
        ),
        migrations.CreateModel(
            name='Meses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mes', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'Meses',
                'ordering': ('id', 'mes'),
            },
        ),
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=5, verbose_name='Código')),
                ('quantidade', models.IntegerField(verbose_name='Quantidade')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Curso')),
            ],
            options={
                'db_table': 'Matricula',
                'ordering': ['curso'],
            },
        ),
    ]
