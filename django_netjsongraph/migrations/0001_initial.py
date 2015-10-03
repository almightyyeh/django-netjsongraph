# -*- coding: utf-8 -*-
# Generated by Django 1.9a1 on 2015-10-03 22:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import jsonfield.fields
import model_utils.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('cost', models.FloatField()),
                ('cost_text', models.CharField(blank=True, max_length=24)),
                ('status', model_utils.fields.StatusField(choices=[('up', 'up'), ('down', 'down')], default='up', max_length=100, no_check_for_status=True)),
                ('properties', jsonfield.fields.JSONField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('label', models.CharField(blank=True, max_length=64)),
                ('addresses', models.CharField(db_index=True, max_length=255)),
                ('properties', jsonfield.fields.JSONField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Topology',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('label', models.CharField(max_length=64, verbose_name='label')),
                ('parser', models.CharField(choices=[('netdiff.OlsrParser', 'OLSRd (txtinfo/jsoninfo)'), ('netdiff.BatmanParser', 'batman-advanced (jsondoc/txtinfo)'), ('netdiff.BmxParser', 'BMX6 (q6m)'), ('netdiff.NetJsonParser', 'NetJSON NetworkGraph'), ('netdiff.CnmlParser', 'CNML 1.0')], help_text='Select topology format', max_length=128, verbose_name='format')),
                ('url', models.URLField(help_text='Topology data will be fetched from this URL', verbose_name='url')),
                ('protocol', models.CharField(blank=True, max_length=64, verbose_name='protocol')),
                ('version', models.CharField(blank=True, max_length=24, verbose_name='version')),
                ('revision', models.CharField(blank=True, max_length=64, verbose_name='revision')),
                ('metric', models.CharField(blank=True, max_length=24, verbose_name='metric')),
            ],
            options={
                'abstract': False,
                'verbose_name_plural': 'topologies',
            },
        ),
        migrations.AddField(
            model_name='link',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='source_node_set', to='netjsongraph.Node'),
        ),
        migrations.AddField(
            model_name='link',
            name='target',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='target_node_set', to='netjsongraph.Node'),
        ),
        migrations.AddField(
            model_name='link',
            name='topology',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='netjsongraph.Topology'),
        ),
    ]
