# Generated by Django 4.1.3 on 2022-11-16 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0002_delete_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_date', models.TimeField(auto_created=True)),
                ('headline_link', models.URLField(blank=True)),
                ('description', models.CharField(max_length=250)),
            ],
        ),
    ]
