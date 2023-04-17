from django.contrib.auth.models import AbstractUser, User
from django.db import models
from geopy import Nominatim


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_image = models.ImageField(upload_to='profile_images/')
    description = models.TextField(blank=True, null=True)
    edit_address = models.BooleanField(default=False)
    edit_machine = models.BooleanField(default=False)
    edit_counter = models.BooleanField(default=False)

    # Дополнительные поля профиля пользователя
    def get_full_name(self):
        """Возвращает полное имя пользователя"""
        return f"{self.user.first_name} {self.user.last_name}"

    def get_username(self):
        """Возвращает имя пользователя"""
        return self.user.username

    def get_profile_image_url(self):
        """Возвращает URL-адрес изображения профиля"""
        return self.profile_image.url

    def get_profile_description(self):
        """Возвращает описание профиля пользователя"""
        return self.description

    def __str__(self):
        return self.user.username


class Address(models.Model):
    """Адресса в которых стоят аппараты"""

    city = models.CharField(max_length=100, verbose_name="Город", help_text="Введите город")
    street = models.CharField(max_length=100, verbose_name="Улица", help_text="Введите улицу")
    house_number = models.CharField(max_length=10, verbose_name="Дом", help_text="Введите номер дома")
    shop_name = models.CharField(max_length=100, verbose_name="Магазин", help_text="Введите магазин где стоит аппарат")

    def __str__(self):
        return f"{self.city}, {self.street} {self.house_number}{self.shop_name}"


    def geo(self):
        geolocator = Nominatim(user_agent="myGeocoder1")  # Измените user_agent на свое значение
        # Адрес, который нужно геокодировать
        address = f'{self.city}, {self.street}, {self.house_number}'

        # Выполняем геокодирование
        location = geolocator.geocode(address)

        if location is not None:
            # Парсим результат
            latitude = location.latitude
            longitude = location.longitude

            # Выводим координаты в лог
            print(f"Широта: {latitude}")
            print(f"Долгота: {longitude}")

            # Возвращаем координаты
            return f'{latitude}, {longitude}'
        else:
            print(f"Ошибка геокодирования для адреса: {address}")
            return None


class Machine(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название аппарата')
    serial_number = models.CharField(max_length=100, verbose_name='Серийный номер', blank=True, null=True, )
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='machines', verbose_name='Адрес')

    def __str__(self):
        return f'{self.name}'
        # f' {self.address.user.username}'

    class Meta:
        verbose_name = 'Аппарат'
        verbose_name_plural = 'Аппараты'

    def get_sum(self):
        try:
            last, pre_last = self.counter.order_by('-month')[:2]
            sum_number = (last.counter_value - pre_last.counter_value) * 10
        except ValueError:
            try:
                last, pre_last = self.counter.last(), 0
                sum_number = (last.counter_value - 0) * 10
            except AttributeError:
                sum_number = 0
        return sum_number


class Counter(models.Model):
    counter_value = models.IntegerField(verbose_name='Значение счетчика')
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE, related_name='counter', default=None)
    month = models.DateTimeField('Дата снятия счетчика', auto_now_add=True, blank=True, null=True)

    class Meta:
        # ordering = ['-month', ]
        verbose_name_plural = 'Счетчики'

    def __str__(self):
        return f'Кран: {self.machine.name} - счетчик: {self.counter_value}'


class CounterWin(models.Model):
    counter_value = models.IntegerField(verbose_name='Значение счетчика', default=0)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Счетчики выигрышей'

    def __str__(self):
        return self.counter_value
