# Generated by Django 3.0.5 on 2020-05-26 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MonHoc', '0009_auto_20200525_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mon',
            name='GioiThieu',
            field=models.FileField(blank=True, default='No file', upload_to=''),
        ),
    ]