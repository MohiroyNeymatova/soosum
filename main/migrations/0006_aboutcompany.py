# Generated by Django 4.1.6 on 2023-11-07 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_infoaboutproduct'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='about/')),
                ('title', models.CharField(max_length=250)),
                ('text', models.TextField()),
            ],
        ),
    ]