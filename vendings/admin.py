from django.contrib import admin
from .models import Address, Machine, Counter, Profile

# Регистрация модели Address в административном интерфейсе
admin.site.register(Address)

# Регистрация модели Machine в административном интерфейсе
admin.site.register(Machine)
admin.site.register(Counter)
admin.site.register(Profile)
