# Generated by Django 4.1.3 on 2022-11-21 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='familia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=22)),
                ('edad', models.IntegerField()),
                ('nacimiento', models.DateField()),
            ],
        ),
    ]
