# Generated by Django 5.0 on 2024-03-08 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('question', models.TextField(max_length=400)),
                ('priority', models.CharField(choices=[('L', 'Low'), ('M', 'Medium'), ('H', 'High')], max_length=1)),
            ],
            options={
                'verbose_name': 'List of Questions',
                'verbose_name_plural': "People's Questions",
            },
        ),
    ]
