# Generated by Django 2.2.5 on 2019-09-28 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joyle_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='animal',
            options={'verbose_name': 'Животные', 'verbose_name_plural': 'Животные'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='electronics',
            options={'verbose_name': 'Электроника', 'verbose_name_plural': 'Электроника'},
        ),
        migrations.AlterModelOptions(
            name='fashionandstyle',
            options={'verbose_name': 'Мода и стиль', 'verbose_name_plural': 'Мода и стиль'},
        ),
        migrations.AlterModelOptions(
            name='forbusiness',
            options={'verbose_name': 'Бизнес', 'verbose_name_plural': 'Бизнес'},
        ),
        migrations.AlterModelOptions(
            name='hobbysport',
            options={'verbose_name': 'Хобби/отдых/спорт', 'verbose_name_plural': 'Хобби/отдых/спорт'},
        ),
        migrations.AlterModelOptions(
            name='property',
            options={'verbose_name': 'Недвижимость', 'verbose_name_plural': 'Недвижимость'},
        ),
        migrations.AlterModelOptions(
            name='store',
            options={'verbose_name': 'Магазин', 'verbose_name_plural': 'Магазины'},
        ),
        migrations.AlterModelOptions(
            name='subanimal',
            options={'verbose_name': 'Подкатег Животные', 'verbose_name_plural': 'Подкатег Животные'},
        ),
        migrations.AlterModelOptions(
            name='subbusiness',
            options={'verbose_name': 'Подкатег бизнеса', 'verbose_name_plural': 'Подкатег бизнеса'},
        ),
        migrations.AlterModelOptions(
            name='subcategelect',
            options={'verbose_name': 'Подкатег электроники', 'verbose_name_plural': 'Подкатег электроники'},
        ),
        migrations.AlterModelOptions(
            name='subcategtransport',
            options={'verbose_name': 'Подкатег транспорта', 'verbose_name_plural': 'Подкатег транспорта'},
        ),
        migrations.AlterModelOptions(
            name='subfashstyle',
            options={'verbose_name': 'Подкатег моды и стиля', 'verbose_name_plural': 'Подкатег моды и стиля'},
        ),
        migrations.AlterModelOptions(
            name='subhobbysport',
            options={'verbose_name': 'Подкатег хобби/отдых/спорт', 'verbose_name_plural': 'Подкатег хобби/отдых/спорт'},
        ),
        migrations.AlterModelOptions(
            name='subproperty',
            options={'verbose_name': 'Подкатег недвижимости', 'verbose_name_plural': 'Подкатег недвижимости'},
        ),
        migrations.AlterModelOptions(
            name='subwork',
            options={'verbose_name': 'Подкатег вакансия', 'verbose_name_plural': 'Подкатег вакансии'},
        ),
        migrations.AlterModelOptions(
            name='work',
            options={'verbose_name': 'Вакансия', 'verbose_name_plural': 'Вакансии'},
        ),
        migrations.AddField(
            model_name='animal',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='electronics',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='fashionandstyle',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='forbusiness',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='hobbysport',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='transport',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='work',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
