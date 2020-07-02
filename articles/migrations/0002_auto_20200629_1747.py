# Generated by Django 3.0.5 on 2020-06-29 20:47

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='article',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name=' Usuario '),
        ),
        migrations.CreateModel(
            name='Zarticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('article', ckeditor.fields.RichTextField(verbose_name=' Articulo : ')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Creado el : ')),
                ('section', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='articles.Zection')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name=' Usuario ')),
            ],
        ),
    ]