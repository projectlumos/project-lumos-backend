# Generated by Django 2.0.2 on 2018-04-02 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain_name', models.CharField(max_length=30)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('icon', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='KnowledgeBase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('skill_level', models.CharField(choices=[('BG', 'BEGINNER'), ('IT', 'INTERMEDIATE'), ('AD', 'ADVANCED')], max_length=10)),
                ('data_type', models.CharField(choices=[('VI', 'VIDEO'), ('BL', 'BLOG'), ('TU', 'TUTORIAL'), ('CO', 'COURSE'), ('OT', 'OTHERS')], max_length=10)),
                ('link_url', models.URLField(max_length=255, unique=True)),
                ('paid', models.BooleanField(default=False)),
                ('project', models.BooleanField(default=False)),
                ('domains', models.ManyToManyField(blank=True, related_name='knowledgebase_domains', to='courses.Domain')),
            ],
            options={
                'ordering': ['-modified_at', '-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_name', models.CharField(max_length=30)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('site_url', models.URLField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('icon', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RandomData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('slug', models.SlugField(unique=True)),
                ('link_url', models.URLField(unique=True)),
                ('data_type', models.CharField(choices=[('VI', 'VIDEO'), ('BL', 'BLOG'), ('TU', 'TUTORIAL'), ('CO', 'COURSE'), ('OT', 'OTHERS')], max_length=2)),
                ('paid', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-modified_at', '-created_at'],
            },
        ),
        migrations.CreateModel(
            name='SoftSkills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('soft_skill_category', models.CharField(max_length=30)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('icon', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SoftSkillsData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('link_url', models.URLField(unique=True)),
                ('data_type', models.CharField(choices=[('VI', 'VIDEO'), ('BL', 'BLOG'), ('TU', 'TUTORIAL'), ('CO', 'COURSE'), ('OT', 'OTHERS')], max_length=2)),
                ('paid', models.BooleanField(default=False)),
                ('soft_skill', models.ManyToManyField(related_name='soft_skills', to='courses.SoftSkills')),
            ],
            options={
                'ordering': ['-modified_at', '-created_at'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='softskills',
            unique_together={('soft_skill_category', 'slug')},
        ),
        migrations.AlterUniqueTogether(
            name='randomdata',
            unique_together={('title', 'slug')},
        ),
        migrations.AlterUniqueTogether(
            name='language',
            unique_together={('language_name', 'slug')},
        ),
        migrations.AddField(
            model_name='knowledgebase',
            name='languages',
            field=models.ManyToManyField(blank=True, related_name='knowledgebase_languages', to='courses.Language'),
        ),
        migrations.AlterUniqueTogether(
            name='domain',
            unique_together={('domain_name', 'slug')},
        ),
        migrations.AlterUniqueTogether(
            name='softskillsdata',
            unique_together={('title', 'slug')},
        ),
        migrations.AlterUniqueTogether(
            name='knowledgebase',
            unique_together={('title', 'slug')},
        ),
    ]
