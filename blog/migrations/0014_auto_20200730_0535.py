# Generated by Django 3.0.3 on 2020-07-30 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20200729_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('uncategorized', 'UNCATEGORIZED'), ('debian', 'DEBIAN'), ('ubuntu', 'UBUNTU'), ('centos', 'CENTOS'), ('redhat', 'REDHAT'), ('archlinux', 'ARCHLINUX')], default='uncategorized', max_length=20),
        ),
    ]
