# Generated by Django 3.2.6 on 2021-08-13 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('name', models.CharField(max_length=50)),
                ('kartinka', models.TextField()),
            ],
            options={
                'verbose_name': 'Коментарий',
                'verbose_name_plural': 'Коментарии',
                'ordering': ['name'],
            },
        ),
        migrations.AlterField(
            model_name='tovary',
            name='photo',
            field=models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Фотки'),
        ),
    ]
