# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-10 07:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('appconf', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dis_name', models.CharField(max_length=50, unique=True, verbose_name='\u8ba4\u8bc1\u6807\u8bc6')),
                ('username', models.CharField(blank=True, max_length=50, verbose_name='\u7528\u6237\u540d')),
                ('password', models.CharField(blank=True, max_length=50, verbose_name='\u5bc6\u7801')),
                ('private_key', models.CharField(blank=True, max_length=100, verbose_name='\u79d8\u94a5')),
                ('desc', models.TextField(blank=True, max_length=200, verbose_name='\u5907\u6ce8\u4fe1\u606f')),
            ],
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.TextField(blank=True, max_length=200, verbose_name='\u9879\u76ee\u63cf\u8ff0')),
                ('deploy_policy', models.CharField(choices=[('', '')], max_length=100, verbose_name='\u90e8\u7f72\u7b56\u7565')),
                ('version', models.CharField(blank=True, max_length=100, verbose_name='\u7248\u672c\u53f7')),
                ('build_clean', models.BooleanField(default=False, verbose_name='\u6e05\u7406\u67b6\u6784')),
                ('rsync_del', models.BooleanField(default=True, verbose_name='\u540c\u6b65\u6e05\u7406')),
                ('shell', models.CharField(blank=True, max_length=200, verbose_name='shell')),
                ('shell_position', models.BooleanField(default=False, verbose_name='\u672c\u5730shell')),
                ('status', models.BooleanField(default=False, verbose_name='\u90e8\u7f72\u72b6\u6001')),
                ('deploy_num', models.IntegerField(default=0, verbose_name='\u90e8\u7f72\u6b21\u6570')),
                ('bar_data', models.IntegerField(default=0)),
                ('auth', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='delivery.AuthInfo', verbose_name='\u8ba4\u8bc1\u4fe1\u606f')),
                ('job_name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='appconf.Project', verbose_name='\u9879\u76ee\u540d')),
            ],
        ),
    ]
