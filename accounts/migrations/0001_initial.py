# Generated by Django 5.0.3 on 2024-04-25 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('phone', models.CharField(max_length=11, unique=True, verbose_name='شماره همراه')),
                ('email', models.EmailField(blank=True, max_length=255, null=True, unique=True, verbose_name='آدرس ایمیل')),
                ('fullname', models.CharField(blank=True, max_length=50, null=True, verbose_name='نام و نام خانوادگی')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال')),
                ('is_admin', models.BooleanField(default=False, verbose_name='ادمین')),
            ],
            options={
                'verbose_name': 'کاربر',
                'verbose_name_plural': 'کاربرها',
            },
        ),
    ]
