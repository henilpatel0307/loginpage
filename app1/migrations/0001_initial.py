# Generated by Django 3.2.3 on 2021-06-04 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company_Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('com_name', models.CharField(default='', max_length=200)),
                ('com_em', models.EmailField(default='', max_length=200)),
                ('com_co', models.PositiveBigIntegerField(default=0)),
                ('com_add', models.TextField(default='')),
                ('join_date', models.DateField(auto_now=True, null=True)),
                ('profile', models.ImageField(default='', max_length=400, upload_to='Com_Profile/')),
                ('com_pass', models.CharField(default='', max_length=200)),
            ],
        ),
    ]
