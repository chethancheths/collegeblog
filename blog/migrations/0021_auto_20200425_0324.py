# Generated by Django 3.0.3 on 2020-04-24 21:54

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_comment_reply'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='desc',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
