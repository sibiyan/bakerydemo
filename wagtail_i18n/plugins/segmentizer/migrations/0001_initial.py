# Generated by Django 2.1.7 on 2019-03-27 14:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('wagtail_i18n', '0009_region_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='HTMLSegment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(unique=True)),
                ('template', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='HTMLSegmentPageLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.TextField()),
                ('html_segment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='page_locations', to='wagtail_i18n_segmentizer.HTMLSegment')),
                ('page_revision', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.PageRevision')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HTMLSegmentText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField()),
                ('html_segment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='text_segments', to='wagtail_i18n_segmentizer.HTMLSegment')),
            ],
        ),
        migrations.CreateModel(
            name='TextSegment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(unique=True)),
                ('text', models.TextField()),
                ('locale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wagtail_i18n.Locale')),
            ],
        ),
        migrations.CreateModel(
            name='TextSegmentPageLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.TextField()),
                ('page_revision', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.PageRevision')),
                ('text_segment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='page_locations', to='wagtail_i18n_segmentizer.TextSegment')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TextSegmentTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('locale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wagtail_i18n.Locale')),
                ('translation_of', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='wagtail_i18n_segmentizer.TextSegment')),
            ],
        ),
        migrations.AddField(
            model_name='htmlsegmenttext',
            name='text_segment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='wagtail_i18n_segmentizer.TextSegment'),
        ),
        migrations.AlterUniqueTogether(
            name='textsegmenttranslation',
            unique_together={('locale', 'translation_of')},
        ),
    ]
