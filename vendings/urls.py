from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path
from .views import AddressListView, AddressDetailView, AddressCreateView, AddressUpdateView, AddressDeleteView, \
    MachineDeleteView, MachineDetailView, \
    MachineUpdateView, MachineCreateView, MachineListView, CounterListView, CounterDetailView, CounterCreateView, \
    CounterUpdateView, \
    CounterDeleteView, ProfileDetailView, CreationLoginView

urlpatterns = [
    # Аппараты
    # Путь для списка адресов
    path('', AddressListView.as_view(), name='address_list'),
    # Путь для подробного адреса
    path('addresses/<int:pk>/detail/', AddressDetailView.as_view(), name='address_detail'),
    # Путь для создания нового адреса
    path('addresses/create/', AddressCreateView.as_view(), name='address_create'),
    # Путь для обновления адреса
    path('addresses/<int:pk>/update/', AddressUpdateView.as_view(), name='address_update'),
    # Путь для удаления адреса
    path('addresses/<int:pk>/delete/', AddressDeleteView.as_view(), name='address_delete'),

    # Аппаратов
    # Путь для списка аппаратов
    path('machine/', MachineListView.as_view(), name='machine_list'),
    # Путь для подробного аппаратов
    path('machine/<int:pk>/detail/', MachineDetailView.as_view(), name='machine_detail'),
    # Путь для создания нового аппаратов
    path('machine/create/', MachineCreateView.as_view(), name='machine_create'),
    # Путь для обновления аппаратов
    path('machine/<int:pk>/update/', MachineUpdateView.as_view(), name='machine_update'),
    # Путь для удаления аппаратов
    path('machine/<int:pk>/delete/', MachineDeleteView.as_view(), name='machine_delete'),
    # Аналогично можно добавить URL-пути для представлений, связанных с моделями Machine и Counter

    # Счетчик
    # Путь для списка адресов
    path('counter/', CounterListView.as_view(), name='counter_list'),
    # Путь для подробного аппаратов
    path('counter/<int:pk>/detail/', CounterDetailView.as_view(), name='counter_detail'),
    # Путь для создания нового адреса
    path('counter/create/', CounterCreateView.as_view(), name='counter_create'),
    # Путь для обновления адреса
    path('counter/<int:pk>/update/', CounterUpdateView.as_view(), name='counter_update'),
    # Путь для удаления адреса
    path('counter/<int:pk>/delete/', CounterDeleteView.as_view(), name='counter_delete'),
    # Аналогично можно добавить URL-пути для представлений, связанных с моделями Machine и Counter
    path('accounts/login/', CreationLoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('accounts/profile/', ProfileDetailView.as_view(), name='profile-detail'),

    # Пример URL-маршрута для профиля пользователя с передачей значения pk
    path('accounts/profile/<int:pk>/', ProfileDetailView.as_view(), name='profile-detail'),

]