# Generated by Django 2.0.4 on 2018-04-07 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_auto_20180407_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipeingredient',
            name='oz',
            field=models.FloatField(blank=True, null=True),
        ),
    ]