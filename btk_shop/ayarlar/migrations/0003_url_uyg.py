# Generated by Django 4.2.6 on 2023-11-07 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ayarlar', '0002_uygulamalar'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='uyg',
            field=models.CharField(default='uyg', max_length=200),
        ),
    ]
