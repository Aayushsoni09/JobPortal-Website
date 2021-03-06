# Generated by Django 3.0.7 on 2020-10-07 16:40

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApplyJob',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jobtitle', models.CharField(max_length=50)),
                ('jobtype', models.CharField(max_length=50)),
                ('apply_date', models.DateTimeField(auto_now=True)),
                ('comname', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Cand_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=250)),
                ('contact', phone_field.models.PhoneField(blank=True, max_length=31)),
                ('gender', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
                ('state', models.CharField(max_length=60)),
                ('district', models.CharField(max_length=60)),
                ('skills', models.CharField(max_length=500)),
                ('experience', models.IntegerField()),
                ('profile_heading', models.CharField(max_length=60)),
                ('qualification', models.CharField(max_length=60)),
                ('image', models.ImageField(upload_to='')),
                ('pincode', models.IntegerField()),
                ('passyear', models.IntegerField()),
                ('cgpa', models.IntegerField()),
                ('extraskills', models.CharField(max_length=500)),
                ('collegename', models.CharField(max_length=200)),
                ('course', models.CharField(max_length=200)),
                ('branch', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cand_name', models.CharField(max_length=50)),
                ('cand_mail', models.EmailField(max_length=254)),
                ('cand_password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=100)),
                ('cmail', models.EmailField(max_length=250)),
                ('cpassword', models.CharField(max_length=50)),
                ('cregdate', models.DateTimeField(auto_now=True)),
                ('cwebsite', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jtitle', models.CharField(max_length=100)),
                ('jskills', models.CharField(max_length=500)),
                ('jdesc', models.CharField(max_length=1000)),
                ('jdate', models.DateTimeField(auto_now=True, null=True)),
                ('jstate', models.CharField(max_length=40)),
                ('jdistrict', models.CharField(max_length=60)),
                ('jcname', models.CharField(default='', max_length=100)),
                ('jobtype', models.CharField(max_length=30)),
                ('min_quali', models.CharField(max_length=30)),
                ('lastapply', models.DateTimeField(null=True)),
                ('maxage', models.IntegerField(default=40)),
                ('no_of_openings', models.IntegerField(default=1)),
            ],
        ),
    ]
