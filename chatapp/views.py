from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from .forms import UserCreationForm, LoginForm
from .models import *
from django.views.generic.edit import CreateView
from django.urls import reverse
def room(request,pk):
    room =  Room.objects.get(id=pk)
    data = Room.objects.all()

    room_messages = room.message_set.all().order_by('createdtime')
    if request.method == 'POST':
        message =Message.objects.create(
            user =request.user,room=room,body=request.POST.get('body'),img=request.FILES.get('imgfield'))
        return redirect('detail',pk=room.id)
    context={'room':room,'messages':room_messages,'data':data}
    return render(request,'index.html',context)

class Ceatepage(CreateView):
    template_name = 'create.html'
    model = Room
    fields = ['name','descreption','img']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    def get_success_url(self):
        return reverse('detail',args=(self.object.id,))


def home(request):
    data = Room.objects.all().order_by('id')
    return render(request,'home.html',context={'data':data})

def user_signup(request):
    p = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        p = 'Nimadur hato ketdi shartlar boyicha kiriting'
    
    else:

        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form ,'p':p})


def user_login(request):
    p = ''
    if request.method == 'POST':
        
        form = LoginForm(request.POST)


        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)    
                return redirect('home')
            p = 'Iltimos togri parol yoki kodni kiriting'

            
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form,'p':p})

def user_logout(request):
    logout(request)
    return redirect('home')