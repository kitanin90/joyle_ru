from django.conf import settings
from django.db import models
from django.utils import timezone


class Client(models.Model):
    lastname = models.CharField(max_length=255, blank=True, verbose_name="Фамилия")
    firstname = models.CharField(max_length=255, blank=True, verbose_name="Имя")
    patronymic = models.CharField(max_length=255, blank=True, verbose_name="Отчество")
    email = models.CharField(max_length=64, unique=True, verbose_name="Почта")

    def fullname(self):
        return '{} {} {}'.format(self.lastname, self.firstname, self.patronymic)

    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Store(models.Model):
    name = models.CharField(max_length=255, blank=True, verbose_name="Название")
    verification = models.BooleanField(verbose_name="Верификация")
    description = models.TextField(blank=True, verbose_name="Описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'


class Category(models.Model):
    name = models.CharField(max_length=255, blank=True, verbose_name="Название")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


# Категория Транспорта
class Subcategtransport(models.Model):
    subcateg_transp_name = models.CharField(max_length=255, blank=True, verbose_name="Название подкатегории")

    def __str__(self):
        return self.subcateg_transp_name

    class Meta:
        verbose_name = 'Подкатег транспорта'
        verbose_name_plural = 'Подкатег транспорта'


class Transport(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    subcateg_transp_name = models.ForeignKey(Subcategtransport, on_delete=models.CASCADE,
                                                verbose_name="Название подкатегории")
    year_of_issue = models.CharField(max_length=255, blank=True, verbose_name="Год выпуска")
    body = models.CharField(max_length=255, blank=True, verbose_name="Кузов")
    mark = models.CharField(max_length=255, blank=True, verbose_name="Марка")
    transmission = models.CharField(max_length=255, blank=True, verbose_name="Коробка передач")
    number_door = models.CharField(max_length=255, blank=True, verbose_name="Количество дверей")
    description = models.CharField(max_length=255, blank=True, verbose_name="Описание")
    owners = models.CharField(max_length=255, blank=True, verbose_name="Количество владельцев")
    power = models.CharField(max_length=255, blank=True, verbose_name="Мощность двигателя")
    price = models.DecimalField(max_digits=50, decimal_places=2, verbose_name="Стоимость")
    photo = models.ImageField(upload_to='Фото')
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def full_title(self):
        return "{} {} {}".format(self.mark, self.year_of_issue, self.power)

    def __str__(self):
        return self.full_title()

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'


# Категория Электроники
class SubcategElect(models.Model):
    name_subcat_electr = models.CharField(max_length=255, blank=True, verbose_name="Название подкатегории")

    def __str__(self):
        return self.name_subcat_electr

    class Meta:
        verbose_name = 'Подкатег электроники'
        verbose_name_plural = 'Подкатег электроники'


class Electronics(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    name_subcat_electr = models.OneToOneField(SubcategElect, on_delete=models.CASCADE, verbose_name="Подкатегория")
    name = models.CharField(max_length=255, blank=True, verbose_name="Название")
    description = models.CharField(max_length=255, blank=True, verbose_name="Описание")
    photo = models.ImageField(upload_to='Фото')
    price = models.DecimalField(max_digits=50, decimal_places=2, verbose_name="Стоимость")
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Электроника'
        verbose_name_plural = 'Электроника'


# Категория Недвижимости
class SubProperty(models.Model):
    nameSubProperty= models.CharField(max_length=255, blank=True, verbose_name="Название подкатегории")

    def __str__(self):
        return self.nameSubProperty

    class Meta:
        verbose_name = 'Подкатег недвижимости'
        verbose_name_plural = 'Подкатег недвижимости'


class Property(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    nameSubProperty = models.OneToOneField(SubProperty,on_delete=models.CASCADE, verbose_name="Подкатегория")
    name = models.CharField(max_length=255, blank=True, verbose_name="Название")
    description = models.CharField(max_length=255, blank=True, verbose_name="Описание")
    photo = models.ImageField(upload_to='Фото')
    price = models.DecimalField(max_digits=50, decimal_places=2, verbose_name="Стоимость")
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Недвижимость'
        verbose_name_plural = 'Недвижимость'


# Категория Работа
class SubWork(models.Model):
    nameSubProperty= models.CharField(max_length=255, blank=True, verbose_name="Название подкатегории")

    def __str__(self):
        return self.nameSubProperty

    class Meta:
        verbose_name = 'Подкатег вакансия'
        verbose_name_plural = 'Подкатег вакансии'


class Work(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    nameSubProperty = models.OneToOneField(SubWork, on_delete=models.CASCADE, verbose_name="Подкатегория")
    name = models.CharField(max_length=255, blank=True, verbose_name="Название")
    description = models.CharField(max_length=255, blank=True, verbose_name="Описание")
    photo = models.ImageField(upload_to='Фото')
    price = models.DecimalField(max_digits=50, decimal_places=2, verbose_name="Стоимость")
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'


# Категория Моды и стиля
class SubFashStyle(models.Model):
    nameSubFashStyle = models.CharField(max_length=255, blank=True, verbose_name="Название подкатегории")

    def __str__(self):
        return self.nameSubFashStyle

    class Meta:
        verbose_name = 'Подкатег моды и стиля'
        verbose_name_plural = 'Подкатег моды и стиля'


class FashionAndStyle(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    nameSubFashStyle = models.OneToOneField(SubFashStyle, on_delete=models.CASCADE, verbose_name="Подкатегория")
    name = models.CharField(max_length=255, blank=True, verbose_name="Название")
    description = models.CharField(max_length=255, blank=True, verbose_name="Описание")
    photo = models.ImageField(upload_to='Фото')
    price = models.DecimalField(max_digits=50, decimal_places=2, verbose_name="Стоимость")
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Мода и стиль'
        verbose_name_plural = 'Мода и стиль'


# Категория Хобби, отдых, спорт
class SubHobbySport(models.Model):
    nameSubHobbySport = models.CharField(max_length=255, blank=True, verbose_name="Название подкатегории")

    def __str__(self):
        return self.nameSubHobbySport

    class Meta:
        verbose_name = 'Подкатег хобби/отдых/спорт'
        verbose_name_plural = 'Подкатег хобби/отдых/спорт'


class HobbySport(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    nameSubHobbySport = models.OneToOneField(SubHobbySport, on_delete=models.CASCADE, verbose_name="Подкатегория")
    name = models.CharField(max_length=255, blank=True, verbose_name="Название")
    description = models.CharField(max_length=255, blank=True, verbose_name="Описание")
    photo = models.ImageField(upload_to='Фото')
    price = models.DecimalField(max_digits=50, decimal_places=2, verbose_name="Стоимость")
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Хобби/отдых/спорт'
        verbose_name_plural = 'Хобби/отдых/спорт'


# Категория Животные
class SubAnimal(models.Model):
    nameSubAnimal = models.CharField(max_length=255, blank=True, verbose_name="Название подкатегории")

    def __str__(self):
        return self.nameSubAnimal

    class Meta:
        verbose_name = 'Подкатег Животные'
        verbose_name_plural = 'Подкатег Животные'


class Animal(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    nameSubAnimal = models.OneToOneField(SubAnimal, on_delete=models.CASCADE, verbose_name="Подкатегория")
    name = models.CharField(max_length=255, blank=True, verbose_name="Название")
    description = models.CharField(max_length=255, blank=True, verbose_name="Описание")
    photo = models.ImageField(upload_to='Фото')
    price = models.DecimalField(max_digits=50, decimal_places=2, verbose_name="Стоимость")
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Животные'
        verbose_name_plural = 'Животные'


# Категория Бизнеса
class SubBusiness(models.Model):
    nameSubAnimal = models.CharField(max_length=255, blank=True, verbose_name="Название подкатегории")

    def __str__(self):
        return self.nameSubAnimal

    class Meta:
        verbose_name = 'Подкатег бизнеса'
        verbose_name_plural = 'Подкатег бизнеса'


class ForBusiness(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    nameSubAnimal = models.OneToOneField(SubBusiness, on_delete=models.CASCADE, verbose_name="Подкатегория")
    name = models.CharField(max_length=255, blank=True, verbose_name="Название")
    description = models.CharField(max_length=255, blank=True, verbose_name="Описание")
    photo = models.ImageField(upload_to='Фото')
    price = models.DecimalField(max_digits=50, decimal_places=2, verbose_name="Стоимость")
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Бизнес'
        verbose_name_plural = 'Бизнес'
