# Generated by Django 3.0.5 on 2020-05-25 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MonHoc', '0008_auto_20200525_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mon',
            name='GioiThieu',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
