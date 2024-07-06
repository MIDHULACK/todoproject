from django.shortcuts import render,redirect
from django.views import View
from todoapp.forms import UserRegisterForm,TodoCreateForm,TodoEditForm,TodoDeleteForm
from todoapp.forms import UserLoginForm
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from todoapp.models import TodoModel
from django.views.generic import TemplateView,CreateView,ListView,UpdateView,DeleteView
from django.urls import reverse_lazy


# Create your views here.
# class Home(View):
#     def get(self,request):
#         return render(request,'home.html')
    

# class LoginPage(View):
#     def get(self,request):
#         return render(request,'home1.html')

class Home(TemplateView):
    template_name='home.html'
class LoginPage(TemplateView):
    template_name='home1.html'

class UserProfileView(View):
    def get(self,request,*args,**kwargs):
        user=User.objects.filter(username=request.user)
        return render(request,'user_profile.html',{'data':user})



class UserViewProfile(View):
    def get(self,request):
        return render(request,'viewprofile.html')    


class UserRegisterView(View):
    def get(self,request):
        form=UserRegisterForm()
        return render(request,'register.html',{'form':form})
    def post(self,request):
        data=UserRegisterForm(request.POST)
        if data.is_valid():
            # data.save()
            formdata=data.cleaned_data
            User.objects.create_user(**formdata)
            return HttpResponse("saved")
        else:
            return HttpResponse("invalid credentials")
        
# authentication-obj=authenticate(username,password)      

class UserLoginView(View):
    def get(self,request):
        form=UserLoginForm()
        return render(request,'login.html',{'form':form})
    

    def post(self,request):
        # data=UserRegisterForm(request.POST)
        uname=request.POST.get("username")
        psw=request.POST.get("password")
        user=authenticate(request,username=uname,password=psw)
        if user:
            login(request,user)
            messages.success(request,'login successful')
            return redirect('home1_view')
        else:
            messages.ERROR(request,'invalidcredential')
            return redirect('home_view')
        
class LogoutView(View):
    def get (self,request):
        logout(request)
        return redirect('home_view')        

# class TodoCreateView(View):
#     def get (self,request):
#         form=TodoCreateForm()
#         return render(request,'todo_create.html',{'form':form})   
#     def post(self,request):
#         data=TodoCreateForm(request.POST)
#         if data.is_valid():
            # title=data.cleaned_data.get('title')
            # content=data.cleaned_data.get('content')
            # user=request.user
            # TodoModel.objects.create(user=user,title=title,content=content)
            # data.instance.user=request.user
            # data.save()
            # return HttpResponse("created")
class TodoCreateView(CreateView):
    form_class=TodoCreateForm
    template_name='todo_create.html'
    model=TodoModel
    # context_object_name="formdata"
    success_url=reverse_lazy('home1_view')

    def form_valid(self,form):
        form.instance.user=self.request.user
        messages.success(self.request,"Task Created Successfully")
        return super().form_valid(form)



# class TodoListView(View):
#     def get(self,request):
#         data=TodoModel.objects.filter(user=request.user)
#         return render(request,'todo_list.html',{'data':data})  

class TodoListView(ListView):
    model=TodoModel
    template_name='todo_list.html'
    context_object_name="data"

    def get_queryset(self):
        return TodoModel.objects.filter(user=self.request.user)

# class TodoEditView(View):
#     def get(self,request,*args,**kwargs):
#         id=kwargs.get('id')
#         task=TodoModel.objects.get(id=id)
#         form=TodoEditForm(instance=task)  
#         return render(request,'todo_edit.html',{'form':form})
     
#     def post(self,request,*args,**kwargs):
#         id=kwargs.get('id')
#         todo_data=TodoModel.objects.get(id=id)
#         data=TodoEditForm(request.POST,instance=todo_data)
#         if data.is_valid():
#             data.save()
#             return redirect('list_view')

class TodoEditView(UpdateView):
    model=TodoModel
    form_class=TodoEditForm
    template_name='todo_edit.html'
    success_url=reverse_lazy('list_view')
    pk_url_kwarg='id'


        
# class TodoDeleteView(View):
#     def get(self,request,*args,**kwargs):
#         id=kwargs.get('id')
#         task=TodoModel.objects.get(id=kwargs.get("id"))
#         task.delete()
#         return redirect('list_view')

class TodoDeleteView(DeleteView):
    model=TodoModel
    pk_url_kwarg='id'  
    success_url=reverse_lazy('list_view') 
    template_name='delete.html'







        



        

