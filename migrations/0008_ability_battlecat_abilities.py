# Generated manually: adds Ability catalog model and links it to BattleCat
# via a many-to-many field, so abilities can be managed as a growing list
# without needing a new migration every time a new ability is added.

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0007_battlecat_traits'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Назва здібності')),
                ('icon', models.ImageField(blank=True, null=True, upload_to='abilities/', verbose_name='Іконка')),
                ('description', models.TextField(blank=True, verbose_name="Опис (наприклад: 'Deals 1.5x damage, only takes 1/2 damage')")),
            ],
            options={
                'verbose_name': 'Здібність',
                'verbose_name_plural': 'Здібності',
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='battlecat',
            name='abilities',
            field=models.ManyToManyField(blank=True, related_name='cats', to='wiki.ability', verbose_name='Здібності'),
        ),
    ]
