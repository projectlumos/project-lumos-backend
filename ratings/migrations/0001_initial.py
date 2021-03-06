# Generated by Django 2.0.2 on 2018-04-02 17:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='KnowledgeBaseRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('attribute_1', models.PositiveSmallIntegerField(choices=[(1, 'ONE'), (2, 'TWO'), (3, 'THREE'), (4, 'FOUR'), (5, 'FIVE')], default=0)),
                ('attribute_2', models.PositiveSmallIntegerField(choices=[(1, 'ONE'), (2, 'TWO'), (3, 'THREE'), (4, 'FOUR'), (5, 'FIVE')], default=0)),
                ('attribute_3', models.PositiveSmallIntegerField(choices=[(1, 'ONE'), (2, 'TWO'), (3, 'THREE'), (4, 'FOUR'), (5, 'FIVE')], default=0)),
                ('attribute_4', models.PositiveSmallIntegerField(choices=[(1, 'ONE'), (2, 'TWO'), (3, 'THREE'), (4, 'FOUR'), (5, 'FIVE')], default=0)),
                ('resource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.KnowledgeBase')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RandomDataRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('attribute_1', models.PositiveSmallIntegerField(choices=[(1, 'ONE'), (2, 'TWO'), (3, 'THREE'), (4, 'FOUR'), (5, 'FIVE')], default=0)),
                ('attribute_2', models.PositiveSmallIntegerField(choices=[(1, 'ONE'), (2, 'TWO'), (3, 'THREE'), (4, 'FOUR'), (5, 'FIVE')], default=0)),
                ('attribute_3', models.PositiveSmallIntegerField(choices=[(1, 'ONE'), (2, 'TWO'), (3, 'THREE'), (4, 'FOUR'), (5, 'FIVE')], default=0)),
                ('attribute_4', models.PositiveSmallIntegerField(choices=[(1, 'ONE'), (2, 'TWO'), (3, 'THREE'), (4, 'FOUR'), (5, 'FIVE')], default=0)),
                ('resource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.RandomData')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SoftSkillsDataRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('attribute_1', models.PositiveSmallIntegerField(choices=[(1, 'ONE'), (2, 'TWO'), (3, 'THREE'), (4, 'FOUR'), (5, 'FIVE')], default=0)),
                ('attribute_2', models.PositiveSmallIntegerField(choices=[(1, 'ONE'), (2, 'TWO'), (3, 'THREE'), (4, 'FOUR'), (5, 'FIVE')], default=0)),
                ('attribute_3', models.PositiveSmallIntegerField(choices=[(1, 'ONE'), (2, 'TWO'), (3, 'THREE'), (4, 'FOUR'), (5, 'FIVE')], default=0)),
                ('attribute_4', models.PositiveSmallIntegerField(choices=[(1, 'ONE'), (2, 'TWO'), (3, 'THREE'), (4, 'FOUR'), (5, 'FIVE')], default=0)),
                ('resource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.SoftSkillsData')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
