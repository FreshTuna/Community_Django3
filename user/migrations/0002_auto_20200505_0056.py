# Generated by Django 2.0.13 on 2020-05-04 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': '커뮤니티 사용자', 'verbose_name_plural': '커뮤니티 사용자 '},
        ),
        migrations.AlterModelTable(
            name='user',
            table='djangojang',
        ),
    ]
