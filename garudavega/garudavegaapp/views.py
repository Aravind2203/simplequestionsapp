from django.shortcuts import render,redirect
from  django.views.generic import CreateView,ListView,DetailView,UpdateView
from django.contrib.auth.decorators import login_required
from .forms import RegisterUser,Additem
from . import forms
from django.contrib.auth import login,logout,authenticate
from .models import Post,Answers
from django.contrib.auth.models import User
# Create your views here.
def rergister_user(request):
    r=RegisterUser()
    if request.method=='POST':
        r=RegisterUser(request.POST)
        if r.is_valid():
            r.save()
            return redirect('login')
    return render(request,'register.html',context={'form':r})

def login_user(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
    return render(request,'login.html')


def home(request):
    posts=Post.objects.all()
    return render(request,'home.html',context={'posts':posts})

def detail(request,pk):
    post=Post.objects.get(id=pk)
    anss=post.answers_set.all()
    
    return render(request,'detail.html',context={'post':post,'anss':anss})
    

@login_required(login_url='login')
def answer(request,args,pk):
    add=forms.Additem()
    add_form=Additem()
    print(type(add_form))
    print(type(add))
    return render(request,'createanswer.html',{'pk':pk,'args':args})

def logout_user(request):
    logout(request)
    return redirect('/')


@login_required(login_url='login')
def answer_to_be_added(request,args,pk):
    if request.method=='POST':
        answer=request.POST['answer']
        if len(answer)>0:
            author=User.objects.get(username=args)
            print(pk)
            post=Post.objects.get(id=pk)
            ANSWER=Answers(author=author,post=post,answer=answer)
            ANSWER.save()
            return redirect('detail',pk=pk)
        else:
            return redirect('a',args=args,pk=pk)


@login_required(login_url='login')
def create_post(request,args):
    if request.method=='POST':
        write=User.objects.get(username=args)
        title=request.POST['title']
        problem=request.POST['problem']

        p=Post(write=write,title=title,problem=problem)
        p.save()
        return redirect('/')
    return render(request,'create.html')


    


