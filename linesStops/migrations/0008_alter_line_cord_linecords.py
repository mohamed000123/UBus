# Generated by Django 3.2.9 on 2021-12-21 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('linesStops', '0007_alter_line_cord_linecords'),
    ]

    operations = [
        migrations.AlterField(
            model_name='line_cord',
            name='LineCords',
            field=models.TextField(),
        ),
    ]