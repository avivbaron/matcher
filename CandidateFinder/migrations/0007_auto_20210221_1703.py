# Generated by Django 2.2.19 on 2021-02-21 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CandidateFinder', '0006_auto_20210221_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='name',
            field=models.CharField(choices=[('Java', 'Java'), ('C', 'C'), ('C++', 'C++'), ('SQL', 'SQL'), ('NodeJS', 'NodeJS'), ('django', 'django'), ('VueJS', 'VueJS'), ('React', 'React')], default='C', max_length=50),
        ),
    ]
