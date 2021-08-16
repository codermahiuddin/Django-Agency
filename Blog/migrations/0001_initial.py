# Generated by Django 3.2 on 2021-08-11 05:20

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogpost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='Md Mahiuddin', max_length=50)),
                ('Title', models.CharField(max_length=250)),
                ('Image', models.ImageField(upload_to='Startup/Blog')),
                ('Description', models.TextField(max_length=5000)),
                ('Time', models.DateTimeField(auto_now_add=True)),
                ('Slug', models.SlugField(unique=True)),
                ('Tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('body', models.TextField(max_length=1000)),
                ('email', models.CharField(max_length=150)),
                ('creation', models.DateTimeField(auto_now_add=True)),
                ('approve', models.BooleanField(default=False)),
                ('Post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='Blog.blogpost')),
            ],
        ),
    ]
