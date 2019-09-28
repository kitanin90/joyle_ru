# Generated by Django 2.2.5 on 2019-09-28 18:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, verbose_name='Название')),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lastname', models.CharField(blank=True, max_length=255, verbose_name='Фамилия')),
                ('firstname', models.CharField(blank=True, max_length=255, verbose_name='Имя')),
                ('patronymic', models.CharField(blank=True, max_length=255, verbose_name='Отчество')),
                ('email', models.CharField(max_length=64, unique=True, verbose_name='Почта')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, verbose_name='Название')),
                ('verification', models.BooleanField()),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='SubAnimal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameSubAnimal', models.CharField(blank=True, max_length=255, verbose_name='Название подкатегории')),
            ],
        ),
        migrations.CreateModel(
            name='SubBusiness',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameSubAnimal', models.CharField(blank=True, max_length=255, verbose_name='Название подкатегории')),
            ],
        ),
        migrations.CreateModel(
            name='SubcategElect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_subcat_electr', models.CharField(blank=True, max_length=255, verbose_name='Название подкатегории')),
            ],
        ),
        migrations.CreateModel(
            name='Subcategtransport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subcateg_transp_name', models.CharField(blank=True, max_length=255, verbose_name='Название подкатегории')),
            ],
        ),
        migrations.CreateModel(
            name='SubFashStyle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameSubFashStyle', models.CharField(blank=True, max_length=255, verbose_name='Название подкатегории')),
            ],
        ),
        migrations.CreateModel(
            name='SubHobbySport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameSubHobbySport', models.CharField(blank=True, max_length=255, verbose_name='Название подкатегории')),
            ],
        ),
        migrations.CreateModel(
            name='SubProperty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameSubProperty', models.CharField(blank=True, max_length=255, verbose_name='Название подкатегории')),
            ],
        ),
        migrations.CreateModel(
            name='SubWork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameSubProperty', models.CharField(blank=True, max_length=255, verbose_name='Название подкатегории')),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, verbose_name='Название')),
                ('description', models.CharField(blank=True, max_length=255, verbose_name='Описание')),
                ('photo', models.ImageField(upload_to='Фото')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Стоимость')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='joyle_app.Category', verbose_name='Категория')),
                ('nameSubProperty', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='joyle_app.SubWork', verbose_name='Подкатегория')),
            ],
        ),
        migrations.CreateModel(
            name='Transport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_of_issue', models.CharField(blank=True, max_length=255, verbose_name='Год выпуска')),
                ('body', models.CharField(blank=True, max_length=255, verbose_name='Кузов')),
                ('mark', models.CharField(blank=True, max_length=255, verbose_name='Марка')),
                ('transmission', models.CharField(blank=True, max_length=255, verbose_name='Коробка передач')),
                ('number_door', models.CharField(blank=True, max_length=255, verbose_name='Количество дверей')),
                ('description', models.CharField(blank=True, max_length=255, verbose_name='Описание')),
                ('owners', models.CharField(blank=True, max_length=255, verbose_name='Количество владельцев')),
                ('power', models.CharField(blank=True, max_length=255, verbose_name='Мощность двигателя')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Стоимость')),
                ('photo', models.ImageField(upload_to='Фото')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='joyle_app.Category', verbose_name='Категория')),
                ('subcateg_transp_name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='joyle_app.Subcategtransport', verbose_name='Название подкатегории')),
            ],
            options={
                'verbose_name': 'Автомобиль',
                'verbose_name_plural': 'Автомобили',
            },
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, verbose_name='Название')),
                ('description', models.CharField(blank=True, max_length=255, verbose_name='Описание')),
                ('photo', models.ImageField(upload_to='Фото')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Стоимость')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='joyle_app.Category', verbose_name='Категория')),
                ('nameSubProperty', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='joyle_app.SubProperty', verbose_name='Подкатегория')),
            ],
        ),
        migrations.CreateModel(
            name='HobbySport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, verbose_name='Название')),
                ('description', models.CharField(blank=True, max_length=255, verbose_name='Описание')),
                ('photo', models.ImageField(upload_to='Фото')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Стоимость')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='joyle_app.Category', verbose_name='Категория')),
                ('nameSubHobbySport', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='joyle_app.SubHobbySport', verbose_name='Подкатегория')),
            ],
        ),
        migrations.CreateModel(
            name='ForBusiness',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, verbose_name='Название')),
                ('description', models.CharField(blank=True, max_length=255, verbose_name='Описание')),
                ('photo', models.ImageField(upload_to='Фото')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Стоимость')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='joyle_app.Category', verbose_name='Категория')),
                ('nameSubAnimal', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='joyle_app.SubBusiness', verbose_name='Подкатегория')),
            ],
        ),
        migrations.CreateModel(
            name='FashionAndStyle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, verbose_name='Название')),
                ('description', models.CharField(blank=True, max_length=255, verbose_name='Описание')),
                ('photo', models.ImageField(upload_to='Фото')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Стоимость')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='joyle_app.Category', verbose_name='Категория')),
                ('nameSubFashStyle', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='joyle_app.SubFashStyle', verbose_name='Подкатегория')),
            ],
        ),
        migrations.CreateModel(
            name='Electronics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, verbose_name='Название')),
                ('description', models.CharField(blank=True, max_length=255, verbose_name='Описание')),
                ('photo', models.ImageField(upload_to='Фото')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Стоимость')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='joyle_app.Category', verbose_name='Категория')),
                ('name_subcat_electr', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='joyle_app.SubcategElect', verbose_name='Подкатегория')),
            ],
        ),
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, verbose_name='Название')),
                ('description', models.CharField(blank=True, max_length=255, verbose_name='Описание')),
                ('photo', models.ImageField(upload_to='Фото')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Стоимость')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='joyle_app.Category', verbose_name='Категория')),
                ('nameSubAnimal', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='joyle_app.SubAnimal', verbose_name='Подкатегория')),
            ],
        ),
    ]
