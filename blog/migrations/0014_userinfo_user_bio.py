# Generated by Django 3.0.3 on 2020-04-17 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_userinfo_user_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='user_bio',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
