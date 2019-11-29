# Generated by Django 2.2.7 on 2019-11-29 04:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type_name', models.CharField(choices=[('MR', 'Mentor'), ('ST', 'Student')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='AppUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.CharField(db_column='bio', default='bio', max_length=1000)),
                ('is_student', models.BooleanField(db_column='is_student', default=False)),
                ('is_mentor', models.BooleanField(db_column='is_mentor', default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
