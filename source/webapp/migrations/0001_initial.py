# Generated by Django 4.1.5 on 2023-01-14 07:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('category', models.TextField(choices=[('other', 'other'), ('pharmacy', 'pharmacy'), ('food', 'food')], max_length=50, verbose_name='content')),
                ('description', models.TextField(blank=True, max_length=2000, null=True, verbose_name='description')),
                ('img', models.ImageField(blank=True, null=True, upload_to='user_avatar', verbose_name='Фото')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=2000, verbose_name='text review')),
                ('rating', models.FloatField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4')], default=0)),
                ('modern', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Время изменения')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.product', verbose_name='Товар')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL, verbose_name='автор')),
            ],
        ),
    ]