# Generated by Django 4.2.1 on 2023-05-22 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_review_stars'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='stars',
            field=models.IntegerField(choices=[(1, '*'), (2, '**'), (3, '***'), (4, '****'), (5, '*****')], null=True),
        ),
    ]
