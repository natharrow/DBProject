# Generated by Django 2.2.7 on 2019-11-29 21:23

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Connection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.PositiveIntegerField(choices=[(0, 'Pending'), (1, 'Accepted'), (2, 'Declined')], db_column='status', default=0, validators=[django.core.validators.MaxValueValidator(2)])),
                ('action_user', models.ForeignKey(db_column='action_user', on_delete=django.db.models.deletion.CASCADE, related_name='action_user', to=settings.AUTH_USER_MODEL)),
                ('user_one', models.ForeignKey(db_column='user_one', on_delete=django.db.models.deletion.CASCADE, related_name='user_one', to=settings.AUTH_USER_MODEL)),
                ('user_two', models.ForeignKey(db_column='user_two', on_delete=django.db.models.deletion.CASCADE, related_name='user_two', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
