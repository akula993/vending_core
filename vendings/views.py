from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy, reverse

from .forms import CounterForm, LoginForm, MachineForm
from .models import Address, Machine, Counter, Profile


# Представление списка адресов
class AddressListView(LoginRequiredMixin, ListView):
    model = Address
    template_name = 'address/address_list.html'  # Замените на имя вашего шаблона
    context_object_name = 'addresses'  # Имя переменной контекста, содержащей список адресов


class AddressDetailView(LoginRequiredMixin, DetailView):
    model = Address
    template_name = 'address/address_detail.html'
    context_object_name = 'address'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        address = self.get_object()
        context['machine_form'] = MachineForm(initial={'address': address})
        return context


    def post(self, request, *args, **kwargs):
        address = self.get_object()
        machine_form = MachineForm(request.POST)
        if machine_form.is_valid():
            machine = machine_form.save(commit=False)
            machine.address = address
            machine.save()
            return redirect('address_detail', pk=address.pk)
        else:
            # Если форма не валидна, обновляем контекст и рендерим снова
            context = self.get_context_data(**kwargs)
            context['machine_form'] = machine_form
            return self.render_to_response(context)
# Представление создания нового адреса
class AddressCreateView(LoginRequiredMixin, CreateView):
    model = Address
    template_name = 'address/address_form.html'  # Замените на имя вашего шаблона
    fields = ['city', 'street', 'house_number', 'shop_name']  # Поля модели, отображаемые в форме создания адреса
    success_url = reverse_lazy('address_list')  # URL-адрес для перенаправления после успешного создания адреса
# Представление обновления адреса
class AddressUpdateView(LoginRequiredMixin, UpdateView):
    model = Address
    template_name = 'address/address_form.html'  # Замените на имя вашего шаблона
    fields = ['city', 'street', 'house_number', 'shop_name']  # Поля модели, отображаемые в форме обновления адреса
    success_url = reverse_lazy('address_list')  # URL-адрес для перенаправления после успешного обновления адреса
# Представление удаления адреса
class AddressDeleteView(LoginRequiredMixin, DeleteView):
    model = Address
    template_name = 'address/address_confirm_delete.html'  # Замените на имя вашего шаблона
    success_url = reverse_lazy('address_list')  # URL-адрес для перенаправления после успешного удаления адреса

# Аналогично можно создать представления для моделей Machine и Counter, используя ListView, CreateView, UpdateView и DeleteView,
# и указав соответствующие модели, шаблоны, поля и URL-адреса.


# Представление списка аппаратов
class MachineListView(LoginRequiredMixin, ListView):
    model = Machine
    template_name = 'machine/machine_list.html'  # Замените на имя вашего шаблона
    context_object_name = 'machines'  # Имя переменной контекста, содержащей список адресов
class MachineDetailView(LoginRequiredMixin, DetailView):
    model = Machine
    template_name = 'machine/machine_detail.html'
    context_object_name = 'machine'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        machine = self.get_object()
        context['counter_form'] = CounterForm(initial={'machine': machine})
        return context

    def post(self, request, *args, **kwargs):
        machine = self.get_object()
        counter_form = CounterForm(request.POST)
        if counter_form.is_valid():
            counter = counter_form.save(commit=False)
            counter.machine = machine
            counter.save()
            # Добавляем сообщение о действии пользователя
            messages.success(request, f'Пользователь {Profile.user} сделал: добавил счетчик')
            return redirect('machine_detail', pk=machine.pk)
        else:
            # Если форма не валидна, обновляем контекст и рендерим снова
            context = self.get_context_data(**kwargs)
            context['counter_form'] = counter_form
            context['notification_message'] = 'Ошибка при добавлении счетчика'

            return self.render_to_response(context)


# Представление создания нового аппаратов
class MachineCreateView(LoginRequiredMixin, CreateView):
    model = Machine
    template_name = 'machine/machine_form.html'  # Замените на имя вашего шаблона
    fields = ['name', 'serial_number', 'address']  # Поля модели, отображаемые в форме создания адреса
    success_url = reverse_lazy('address_list')  # URL-адрес для перенаправления после успешного создания адреса


    def get_success_url(self):
        machine = self.get_object()
        return reverse('address_detail', args=[str(machine.address.pk)])
# Представление обновления аппаратов
class MachineUpdateView(LoginRequiredMixin, UpdateView):
    model = Machine
    template_name = 'machine/machine_form.html'  # Замените на имя вашего шаблона
    fields = ['name', 'serial_number',]  # Поля модели, отображаемые в форме обновления адреса
    # success_url = reverse_lazy('address_list')  # URL-адрес для перенаправления после успешного обновления адреса


    def get_success_url(self):
        machine = self.get_object()
        return reverse('machine_detail', args=[str(machine.address.pk)])
# Представление удаления аппаратов
class MachineDeleteView(LoginRequiredMixin, DeleteView):
    model = Machine
    template_name = 'machine/machine_confirm_delete.html'  # Замените на имя вашего шаблона
    # success_url = reverse_lazy('address_list')  # URL-адрес для перенаправления после успешного удаления адреса

    def get_success_url(self):
        machine = self.get_object()
        return reverse('address_detail', args=[str(machine.address.pk)])

# Представление списка аппаратов
class CounterListView(LoginRequiredMixin, ListView):
    model = Counter
    template_name = 'counter/counter_list.html'  # Замените на имя вашего шаблона
    context_object_name = 'counters'  # Имя переменной контекста, содержащей список адресов


    def get_success_url(self):
        counter = self.get_object()
        return reverse('machine_detail', args=[str(counter.machine.pk)])
class CounterDetailView(LoginRequiredMixin, DetailView):
    model = Counter
    template_name = 'address/address_detail.html'
    context_object_name = 'counter'

    def get_success_url(self):
        counter = self.get_object()
        return reverse('machine_detail', args=[str(counter.machine.pk)])
# Представление создания нового аппаратов
class CounterCreateView(LoginRequiredMixin, CreateView):
    model = Counter
    template_name = 'counter/counter_form.html'  # Замените на имя вашего шаблона
    fields = ['counter_value', 'machine']  # Поля модели, отображаемые в форме создания адреса
    success_url = reverse_lazy('address_list')  # URL-адрес для перенаправления после успешного создания адреса
    def form_valid(self, form):
        # Добавляем сообщение о действии пользователя
        messages.success(self.request, f'Пользователь {self.request.user.username} сделал: создал счетчик')
        return super().form_valid(form)

    def get_success_url(self):
        counter = self.get_object()
        return reverse('machine_detail', args=[str(counter.machine.pk)])
# Представление обновления аппаратов
class CounterUpdateView(LoginRequiredMixin, UpdateView):
    model = Counter
    template_name = 'counter/counter_form.html'  # Замените на имя вашего шаблона
    # fields = ['counter_value', 'machine', 'month']  # Поля модели, отображаемые в форме обновления адреса
    success_url = reverse_lazy('address_list')  # URL-адрес для перенаправления после успешного обновления адреса
    form_class = CounterForm

    def form_valid(self, form):
        # Добавляем сообщение о действии пользователя
        messages.success(self.request, f'Пользователь {self.request.user.username} сделал: обновил счетчик')
        return super().form_valid(form)
    def get_success_url(self):
        counter = self.get_object()
        return reverse('machine_detail', args=[str(counter.machine.pk)])
# Представление удаления аппаратов
class CounterDeleteView(LoginRequiredMixin, DeleteView):
    model = Counter
    template_name = 'counter/counter_confirm_delete.html'  # Замените на имя вашего шаблона
    success_url = reverse_lazy('address_list')  # URL-адрес для перенаправления после успешного удаления адреса

    def delete(self, request, *args, **kwargs):
        # Добавляем сообщение о действии пользователя
        messages.success(request, f'Пользователь {request.user.username} сделал: удалил счетчик')
        return super().delete(request, *args, **kwargs)
    def get_success_url(self):
        counter = self.get_object()
        return reverse('machine_detail', args=[str(counter.machine.pk)])

class CreationLoginView(LoginView):
    template_name = 'accounts/login.html'  # имя шаблона страницы входа
    # success_url = reverse_lazy('address_list')  # URL, на который перенаправлять после успешного входа
    authentication_form = LoginForm

class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'accounts/profile_detail.html'
    context_object_name = 'profile'
