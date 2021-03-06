# Generated by Django 3.1.6 on 2021-02-13 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Territory',
            fields=[
                ('code', models.CharField(max_length=19, primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('level', models.IntegerField()),
                ('category', models.CharField(choices=[('О', 'Область або АРК'), ('К', 'Місто, що має спеціальний статус'), ('Р', 'Район в області або в АРК'), ('Н', 'Територіальна громада'), ('М', 'Місто'), ('Т', 'Селище міського типу'), ('С', 'Село'), ('Х', 'Селище'), ('В', 'Район в місті')], max_length=1)),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='territories.territory')),
            ],
        ),
    ]
