from django import forms
from django.forms import widgets
from django.contrib.auth.forms import AuthenticationForm
from .models import Auto

class LoginForm(AuthenticationForm):
    
    def __init__(self, request=None, *args, **kwargs):
        super(LoginForm, self).__init__(request=request, *args, **kwargs)
        
class AutoForm(forms.ModelForm):
    
    class Meta:
        model = Auto
        fields= '__all__'
        widgets = {
            'image': forms.FileInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'marca': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'modelo': forms.TextInput(
                attrs={
                    'class': 'form-control'
                    
                }
            ),
            'combustible': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'precio': forms.TextInput(
                attrs={
                    'class': 'form-control'     
                }
            ),
            'año': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }  
            ),
            'color': forms.TextInput(
                attrs={
                    'class': 'form-control',
                
                }
            ),
            'tipo_vehiculo': forms.TextInput(
                attrs={
                    'class': 'form-control',
                
                }
            ),
            'tipo_caja': forms.TextInput(
                attrs={
                    'class': 'form-control',
                
                }
            ),
             'aire_acondicionado': forms.TextInput(
                attrs={
                    'class': 'form-control',
                
                }
            ),
            'alzavidrios': forms.TextInput(
                attrs={
                    'class': 'form-control',
                
                }
            ),
            'direccion_hidraulica': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    
                }
            ),
            'cierre_puerta': forms.TextInput(
                attrs={
                    'class': 'form-control',
                
                }
            ),
            'tranmision_auto': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    
                }
            ),
            'espejos': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    
                }
            ),
             'airbagas': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    
                }
            ),
              'radio': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    
                }
            )          
        }