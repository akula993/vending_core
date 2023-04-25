from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path
from django.views.decorators.cache import cache_page
from django.views.generic import TemplateView

from .views import AddressListView, AddressDetailView, AddressCreateView, AddressUpdateView, AddressDeleteView, \
    MachineDeleteView, MachineDetailView, \
    MachineUpdateView, MachineCreateView, MachineListView, CounterListView, CounterDetailView, CounterCreateView, \
    CounterUpdateView, \
    CounterDeleteView, ProfileDetailView, CreationLoginView

urlpatterns = [
    # Аппараты
    # Путь для списка адресов
    path('', cache_page(60 * 180)(AddressListView.as_view()), name='address_list'),
    # Путь для подробного адреса
    path('addresses/<int:pk>/detail/', cache_page(60 * 180)(AddressDetailView.as_view()), name='address_detail'),
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
    # ТЕСТ
    # Аппараты
    # Путь для списка адресов
    path('test/', AddressListView.as_view(template_name='test/address/list.html'), name='address_list_test'),
    # Путь для подробного адреса
    path('test/<int:pk>/detail/', AddressDetailView.as_view(template_name='test/address/detail.html'),
         name='address_detail_test'),
    # Путь для создания нового адреса
    path('test/addresses/create/', AddressCreateView.as_view(template_name='test/address/create.html'),
         name='address_create_test'),
    # Путь для обновления адреса
    path('test/addresses/<int:pk>/update/', AddressUpdateView.as_view(template_name='test/address/update.html'),
         name='address_update_test'),
    # Путь для удаления адреса
    path('test/addresses/<int:pk>/delete/', AddressDeleteView.as_view(template_name='test/address/delete.html'),
         name='address_delete_test'),
]
