# Generated by Django 5.0.6 on 2024-05-21 16:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='product',
        ),
        migrations.RemoveField(
            model_name='rating',
            name='user',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='user',
        ),
        migrations.RemoveField(
            model_name='wishlist',
            name='user',
        ),
        migrations.RemoveField(
            model_name='wishlist',
            name='product',
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Like',
        ),
        migrations.DeleteModel(
            name='Rating',
        ),
        migrations.DeleteModel(
            name='UserInfo',
        ),
        migrations.DeleteModel(
            name='WishList',
        ),
    ]
