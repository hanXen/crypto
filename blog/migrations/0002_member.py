# Generated by Django 2.2.1 on 2019-05-08 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(default='Researcher', max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(blank=True, max_length=200, null=True)),
                ('thumb', models.URLField(blank=True, null=True)),
                ('desc', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
