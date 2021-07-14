from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.contrib.auth import login
from django.contrib.messages import success
from django.views.decorators.csrf import csrf_protect
from .models import Auto
from app.forms import LoginForm, AutoForm
from django.views.generic.edit import CreateView, UpdateView, FormView, DeleteView
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from app.mixins import  ValidatePermissionRequiredMixin
# Create your views here.

class MenuAuto(ListView):
    template_name = 'views/menu.html'
    queryset =Auto.objects.all()
    context_object_name='autos'
    
class Products(ListView):
    template_name= 'views/models_products.html'
    queryset=Auto.objects.all()
    context_object_name='autos'
                            
class AutoList (LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):
    model = Auto
    template_name ='views/list_products.html'
    queryset = Auto.objects.all()
    context_object_name = 'autos'
    
    
class LoginView(FormView):
    
    template_name = 'views/auth/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('app:menu')
    
    @method_decorator(never_cache)
    @method_decorator(csrf_protect)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse_lazy('app:menu'))
        return super(FormView, self).dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(LoginView, self).form_valid(form)
    
    

class AutoCreate(LoginRequiredMixin, ValidatePermissionRequiredMixin,CreateView):
    model = Auto
    success_url = reverse_lazy('app:autos_list')
    template_name= 'views/autos/forms/create.html'
    form_class = AutoForm
    def form_valid(self, form):
        success(self.request, 'Se creó el auto con éxito')
        return super().form_valid(form)
    

class AutoDelete(LoginRequiredMixin, ValidatePermissionRequiredMixin,DeleteView):
    model = Auto
    success_url = reverse_lazy('app:autos_list')
    template_name= 'views/autos/forms/delete.html'
    
    
    def form_valid(self, form):
        success(self.request, 'Se eliminó el auto con éxito')
        return super().form_valid(form)
    
 
class AutoUpdate(LoginRequiredMixin, ValidatePermissionRequiredMixin,UpdateView):
    model = Auto
    form_class = AutoForm
    success_url = reverse_lazy('app:autos_list')
    template_name= 'views/autos/forms/update.html'
    
    def form_valid(self, form):
        success(self.request, 'Se actualizó el auto con éxito')
        return super().form_valid(form)
    
class DetailList(LoginRequiredMixin, ListView):
    permission_required = 'app.view_Auto'
    model=Auto
    template_name='views/detail_list.html'
    queryset=Auto.objects.all()
    context_object_name='autos'
    
    def list_valid(self):
        return redirect(reverse_lazy('app:detail_list'))