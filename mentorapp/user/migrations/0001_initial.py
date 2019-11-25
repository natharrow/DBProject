# Generated by Django 2.2.7 on 2019-11-25 01:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type_name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=40)),
                ('email_address', models.CharField(max_length=50)),
                ('bio', models.CharField(default='bio', max_length=1000)),
                ('user_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.UserType')),
            ],
        ),
    ]
