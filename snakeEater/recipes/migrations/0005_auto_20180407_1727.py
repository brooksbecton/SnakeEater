# Generated by Django 2.0.4 on 2018-04-07 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_auto_20180404_2015'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipeingredient',
            old_name='ingredientId',
            new_name='ingredient',
        ),
        migrations.RenameField(
            model_name='recipeingredient',
            old_name='recipeId',
            new_name='recipe',
        ),
        migrations.AlterField(
            model_name='recipeingredient',
            name='oz',
            field=models.FloatField(),
        ),
    ]
