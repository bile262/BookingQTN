# Generated by Django 2.2.6 on 2019-12-18 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phong', '0005_auto_20191218_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phong',
            name='loaiphong',
            field=models.IntegerField(choices=[(2, 'Cao cấp'), (0, 'Thường'), (1, 'Trung bình')], default=0),
        ),
    ]
