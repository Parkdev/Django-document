# Generated by Django 2.1.2 on 2018-10-08 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fields', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='age2',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='age3',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='shirt_size',
            field=models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], max_length=1),
        ),
    ]
