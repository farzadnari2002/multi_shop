# Generated by Django 5.0.3 on 2024-04-25 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_user_options_remove_user_firstname_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='fullname',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='نام و نام خانوادگی'),
        ),
    ]
