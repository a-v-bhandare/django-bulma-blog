# Generated by Django 2.2.2 on 2019-07-07 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20190630_1805'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='disqus_support',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='article',
            name='summary',
            field=models.CharField(default='', max_length=160),
        ),
    ]
