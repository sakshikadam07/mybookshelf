# Generated by Django 4.2 on 2024-03-23 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0003_alter_category_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
