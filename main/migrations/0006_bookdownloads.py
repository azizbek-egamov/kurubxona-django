# Generated by Django 4.2.11 on 2024-06-13 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_delete_statistika_category_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookDownloads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
            ],
        ),
    ]
