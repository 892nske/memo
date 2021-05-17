# Generated by Django 3.2.3 on 2021-05-17 02:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TagName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_id', models.IntegerField()),
                ('tag_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('memo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.memo')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.tagname')),
            ],
        ),
    ]