# Generated by Django 4.0.4 on 2022-06-02 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='imageUrl',
            field=models.URLField(default='https://picsum.photos/seed/picsum/200/300'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
