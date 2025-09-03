#!/usr/bin/env python
"""
Script to create initial migrations for userprofile app
This works around Python 3.13 compatibility issues with Django 5.1.7
"""
import os
import sys
import django
from django.conf import settings
from django.core.management import execute_from_command_line

# Add the project directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pickle_pro.settings')

# Setup Django
django.setup()

try:
    # Try to create migrations for userprofile app
    from django.core.management.commands.makemigrations import Command as MakeMigrationsCommand
    from django.core.management.base import CommandError
    
    command = MakeMigrationsCommand()
    
    # Create migrations for userprofile app specifically
    command.handle(
        verbosity=2,
        interactive=False,
        dry_run=False,
        merge=False,
        empty=False,
        app_labels=['userprofile']
    )
    
    print("✅ Successfully created migrations for userprofile app!")
    
except Exception as e:
    print(f"❌ Error creating migrations: {e}")
    print("This is likely due to Python 3.13 compatibility issues with Django 5.1.7")
    
    # Manual migration creation as fallback
    print("\n🔧 Creating manual migration file...")
    
    migration_content = '''# Generated manually for Python 3.13 compatibility
from django.db import migrations, models
import django.contrib.auth.models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('full_name', models.CharField(blank=True, max_length=30, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=10, null=True)),
                ('otp', models.CharField(blank=True, max_length=6, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='static/assets/images')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='userprofile.category')),
            ],
        ),
    ]
'''
    
    # Write the manual migration file
    migration_file_path = 'userprofile/migrations/0001_initial.py'
    try:
        with open(migration_file_path, 'w') as f:
            f.write(migration_content)
        print(f"✅ Manual migration file created: {migration_file_path}")
    except Exception as write_error:
        print(f"❌ Error writing migration file: {write_error}")
