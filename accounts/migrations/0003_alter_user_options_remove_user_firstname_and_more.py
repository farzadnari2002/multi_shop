# Generated by Django 5.0.3 on 2024-04-25 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_user_firstname_alter_user_lastname'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'کاربر', 'verbose_name_plural': 'کاربرها'},
        ),
        migrations.RemoveField(
            model_name='user',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='user',
            name='lastname',
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(default=True, max_length=12, unique=True, verbose_name='شماره همراه'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=255, null=True, unique=True, verbose_name='آدرس ایمیل'),
        ),
    ]
