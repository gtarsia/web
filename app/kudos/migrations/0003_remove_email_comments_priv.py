# Generated by Django 2.0.7 on 2018-08-30 19:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kudos', '0002_remove_email_expires_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='email',
            name='comments_priv',
        ),
    ]