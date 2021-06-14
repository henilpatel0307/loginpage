# Generated by Django 3.2.3 on 2021-06-04 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Table1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_nm', models.CharField(blank=True, default='', max_length=200, null=True, verbose_name='Employee Name')),
                ('emp_id', models.PositiveBigIntegerField(default=0, verbose_name='Emploee IDS')),
                ('emp_em', models.EmailField(blank=True, default='', max_length=200, null=True, verbose_name='Emploee Email ID')),
                ('emp_cno', models.IntegerField(default=0, verbose_name='Employee Contact Number')),
                ('emp_add1', models.TextField(default=0, verbose_name='Employee Address1')),
                ('emp_add2', models.TextField(default=0, verbose_name='Employee Address2')),
            ],
        ),
    ]