# Generated by Django 2.2.7 on 2019-12-10 02:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_user', '0003_auto_20191210_0229'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='name',
            new_name='company_name',
        ),
        migrations.RenameField(
            model_name='industry',
            old_name='name',
            new_name='industry_type_name',
        ),
        migrations.RenameField(
            model_name='major',
            old_name='name',
            new_name='major_name',
        ),
        migrations.RenameField(
            model_name='school',
            old_name='name',
            new_name='school_name',
        ),
    ]