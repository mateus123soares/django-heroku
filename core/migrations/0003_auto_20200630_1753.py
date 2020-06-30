# Generated by Django 3.0.7 on 2020-06-30 17:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200627_2041'),
    ]

    operations = [
        migrations.CreateModel(
            name='ID',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='client',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='clients'),
        ),
        migrations.AddField(
            model_name='client',
            name='doc_id',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.ID'),
        ),
    ]
