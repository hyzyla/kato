# Generated by Django 3.1.6 on 2021-02-13 22:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('territories', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='territory',
            options={'verbose_name_plural': 'Territories'},
        ),
        migrations.AddField(
            model_name='territory',
            name='children_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='territory',
            name='category',
            field=models.CharField(choices=[('O', 'Область або АРК'), ('K', 'Місто, що має спеціальний статус'), ('P', 'Район в області або в АРК'), ('H', 'Територіальна громада'), ('M', 'Місто'), ('T', 'Селище міського типу'), ('C', 'Село'), ('X', 'Селище'), ('B', 'Район в місті')], max_length=1),
        ),
        migrations.AlterField(
            model_name='territory',
            name='name',
            field=models.CharField(max_length=1028),
        ),
        migrations.AlterField(
            model_name='territory',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='territories.territory'),
        ),
    ]