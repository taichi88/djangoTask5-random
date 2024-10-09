from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import HouseModel, UserModel
from .forms import HouseForm, UserForm
from django.urls import reverse_lazy
# Create your views here.



class HouseCreateView(CreateView):
    model = HouseModel
    form_class = HouseForm
    template_name = 'house/house_edit.html'
    success_url = reverse_lazy('house_list') #url-ში როცა შევქმნი house list იქ დაერქმევა ეს
    
class HouseListView(ListView):
    model = HouseModel
    template_name = 'home/house_list.html'
    context_object_name = 'house'

class HouseDetailView(DetailView):
    model = HouseModel
    template_name = 'home/house_detail.html'

class HouseUpdateView(UpdateView):
    model = HouseModel
    form_class = HouseForm
    template_name = 'home/house_edit.html'
    success_url = reverse_lazy('house_list')

class HouseDeleteView(DeleteView):
    model = HouseModel
    template_name = 'home/house_confirm_delete.html'
    success_url = reverse_lazy('house_list')   



class UserCreateView(CreateView):
    model = UserModel
    form_class = UserForm
    template_name = 'user/user_edit.html'
    success_url = reverse_lazy('user_list')

class UserListView(ListView):
    model = UserModel
    template_name = 'user/user_list.html'
    context_object_name = 'users'

class UserDetailView(DetailView):
    model = UserModel
    template_name = 'user/user_detail.html'

class UserUpdateView(UpdateView):
    model = UserModel
    form_class = UserForm
    template_name = 'user/user_edit.html'
    success_url = reverse_lazy('user_list')

class UserDeleteView(DeleteView):
    model = UserModel
    template_name = 'user/user_confirm_delete.html'
    success_url = reverse_lazy('user_list')