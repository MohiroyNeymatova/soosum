# Generated by Django 4.1.6 on 2023-11-07 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_diseasebanner_delete_diseaseimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='HowToUse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bg_image', models.ImageField(upload_to='images/')),
                ('title', models.CharField(max_length=250)),
                ('text', models.TextField()),
            ],
        ),
    ]
