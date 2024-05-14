# Generated by Django 4.2 on 2024-05-14 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_app', '0004_delete_userotp'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserOtp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('otp', models.CharField(max_length=6)),
            ],
        ),
    ]
