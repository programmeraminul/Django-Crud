# Generated by Django 4.0.3 on 2022-08-30 06:37

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion
import django_json_field_schema_validator.validators
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='logIn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=70)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='roles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roleName', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='signUp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=20)),
                ('lastName', models.CharField(max_length=20)),
                ('userName', models.CharField(default=None, max_length=50)),
                ('email', models.EmailField(default=None, max_length=70)),
                ('password', models.CharField(max_length=200)),
                ('userRoll', models.CharField(choices=[('user', 'User'), ('admin_1', 'Admin_1'), ('admin_2', 'Admin_2'), ('super_admin', 'Super Admin')], default=None, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='singleImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imgname', models.CharField(max_length=150)),
                ('myImg', models.ImageField(max_length=150, upload_to='')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud.signup')),
            ],
        ),
        migrations.CreateModel(
            name='setFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jpg_image', models.ImageField(upload_to='')),
                ('png_image', models.ImageField(upload_to='')),
                ('audio', models.FileField(upload_to='')),
                ('video', models.FileField(upload_to='')),
                ('pdf', models.FileField(upload_to='')),
                ('text', models.FileField(upload_to='')),
                ('doc', models.FileField(upload_to='')),
                ('html', models.FileField(upload_to='')),
                ('css', models.FileField(upload_to='')),
                ('java', models.FileField(upload_to='')),
                ('psd', models.FileField(upload_to='')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud.signup')),
            ],
        ),
        migrations.CreateModel(
            name='setField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dropdown', models.CharField(choices=[('blue', 'Blue'), ('black', 'Black'), ('green', 'Green')], default='blue', max_length=100)),
                ('choice', models.CharField(max_length=100)),
                ('multichoice', models.CharField(max_length=100)),
                ('characterField', models.CharField(max_length=100)),
                ('textField', models.TextField(max_length=100)),
                ('intField', models.IntegerField()),
                ('dateField', models.DateField()),
                ('timeField', models.TimeField()),
                ('datetimeField', models.DateField()),
                ('decimalField', models.DecimalField(decimal_places=2, max_digits=20)),
                ('emailField', models.EmailField(max_length=254, verbose_name='Enter Email')),
                ('floatField', models.FloatField()),
                ('positiveintField', models.PositiveIntegerField()),
                ('positivebigintField', models.PositiveBigIntegerField()),
                ('positivesmallintField', models.PositiveSmallIntegerField()),
                ('smallintField', models.SmallIntegerField()),
                ('bigintField', models.BigIntegerField()),
                ('uuidField', models.UUIDField(default=uuid.uuid4)),
                ('durationField', models.DurationField()),
                ('jsonField', models.JSONField(null=True, validators=[django_json_field_schema_validator.validators.JSONFieldSchemaValidator])),
                ('slugField', models.SlugField()),
                ('urlField', models.URLField()),
                ('genericipaddrsField', models.GenericIPAddressField()),
                ('image', models.ImageField(upload_to='')),
                ('autoslugField', autoslug.fields.AutoSlugField(default=None, editable=False, populate_from='characterField', unique=True)),
                ('binaryField', models.BinaryField(default=1)),
                ('passwordField', models.TextField(default=None)),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud.signup')),
            ],
        ),
    ]
