# Generated by Django 4.1 on 2022-08-26 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('desc', models.TextField()),
                ('image', models.ImageField(upload_to='pics')),
                ('price', models.PositiveIntegerField()),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
