# Generated by Django 2.2.5 on 2020-09-01 12:17

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('name', models.CharField(blank=True, max_length=20)),
                ('school', models.CharField(blank=True, max_length=10)),
                ('grade', models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)], null=True)),
                ('group', models.IntegerField(blank=True, null=True)),
                ('number', models.IntegerField(blank=True, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=10, null=True)),
                ('teacher', models.BooleanField(default=False)),
                ('bio', models.TextField(blank=True, null=True)),
                ('email_verified', models.BooleanField(default=False)),
                ('email_secret', models.CharField(blank=True, default='', max_length=20)),
                ('login_method', models.CharField(choices=[('email', 'Email'), ('github', 'Github'), ('kakao', 'Kakao')], default='email', max_length=50)),
                ('pacer', models.IntegerField(blank=True, default=0, null=True)),
                ('longTimeRun', models.IntegerField(blank=True, default=0, null=True)),
                ('stepTest', models.IntegerField(blank=True, default=0, null=True)),
                ('bendFoward', models.IntegerField(blank=True, default=0, null=True)),
                ('totalFlexibility', models.IntegerField(blank=True, default=0, null=True)),
                ('pushUp', models.IntegerField(blank=True, default=0, null=True)),
                ('sitUp', models.IntegerField(blank=True, default=0, null=True)),
                ('grip', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, null=True)),
                ('sprint', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, null=True)),
                ('longJump', models.DecimalField(blank=True, decimal_places=1, default=0, max_digits=5, null=True)),
                ('height', models.DecimalField(decimal_places=1, default=0, max_digits=5)),
                ('weight', models.DecimalField(decimal_places=1, default=0, max_digits=5)),
                ('fat', models.DecimalField(blank=True, decimal_places=1, default=0, max_digits=5, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
