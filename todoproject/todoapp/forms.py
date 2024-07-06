from django import forms
from django.contrib.auth.models import User
from todoapp.models import TodoModel


class UserRegisterForm(forms.ModelForm):
    class Meta:
        model=User
        #fields="__all__"
        fields=["first_name","last_name","email","username","password"]
        #exclude=["is_user"]


class UserLoginForm(forms.ModelForm):
    class Meta:
        model=User
        #fields="__all__"
        fields=["username","password"]
        #exclude=["is_user"]     

class TodoCreateForm(forms.ModelForm):
    class Meta:
        model=TodoModel
        exclude=['user','status']
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'content':forms.TextInput(attrs={'class':'form-control'})
        }        



class TodoEditForm(forms.ModelForm):
    class Meta:
        model=TodoModel
        exclude=['user']
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'content':forms.TextInput(attrs={'class':'form-control'}),
            'status':forms.CheckboxInput(attrs={'class':'form-check-input'})
        }        
class TodoDeleteForm(forms.ModelForm):
    class Meta:
        model=TodoModel
        exclude=['user']
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'content':forms.TextInput(attrs={'class':'form-control'}),
            'status':forms.CheckboxInput(attrs={'class':'form-check-input'})
        }        
