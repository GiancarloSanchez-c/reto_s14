from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import  csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages

class isSuperMixins(object):
    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        return redirect('logout')
    
    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(self).form_valid(form)    
    
class ValidatePermissionRequiredMixin(object):
    
    permission_required =''
    url_redirect= None
    
    def get_perms(self):
        if isinstance(self.permission_required, str):
            perms = (self.permission_required,)
        else:
            perms = self.permission_required
        return perms
    
    def get_url_redirect(self):
        if self.url_redirect is None:
            return reverse_lazy('login')
        return self.url_redirect
        
    def dispatch(self, request, *args, **kwargs):
        if request.user.has_perms(self.get_perms()):
            return super().dispatch(request, *args, **kwargs)
        else: 
            messages.error(request,('No tienes permiso para entrar a esta opcion'))
        return redirect(self.get_url_redirect())