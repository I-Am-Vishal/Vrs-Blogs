
from typing import ContextManager
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate,login,logout
from django.urls.conf import include
from blog.models import BlogModel,Query
import math
from .forms import BlogForm


# ------------------------------------------------------------------------------------------------------------------------------------------------


def home(request):
    return render(request,"blog/blog-home.html")

# ------------------------------------------------------------------------------------------------------------------------------------------------

def create(request):

    users=User.objects.all()
    current_user=request.user
    context={ 'users':users,'current_user':current_user}
    if request.method=='POST':

        author=User.objects.get(username=request.user)
        Title= request.POST['title']
        Description = request.POST['Descr']
        Content = request.POST['cont']

        Blog_Posts=BlogModel.objects.create(author=author,title=Title,description=Description,content=Content)
        Blog_Posts.save()
        messages.info(request,'Your Blog has been created successfully')
        return redirect('create')
     
    else:
        return render(request,"blog/blog-create.html",context)

# ------------------------------------------------------------------------------------------------------------------------------------------------

def blog(request):

    users=User.objects.all()

    no_of_posts = 4

    page=request.GET.get('page')

    if page is None:
        page=1
    else:
        page=int(page)

    blogs=BlogModel.objects.all()
    length=len(blogs)
    blogs=blogs[(page-1)*no_of_posts: page*no_of_posts]

    if page > 1:

        prev=page-1

    else:

        prev=None

    if page < math.ceil(length/no_of_posts):

        next=page+1

    else:

        next=None


    context={ 'blogs':blogs,'prev':prev,'next':next,'users':users}
    return render(request,"blog/blog-blog.html",context)

  
# ------------------------------------------------------------------------------------------------------------------------------------------------


def search(request):

    query=request.GET['query']
    blogs=BlogModel.objects.filter(title__icontains=query)
    context={'blogs':blogs}
    return render(request,"blog/blog-search.html",context)

# ------------------------------------------------------------------------------------------------------------------------------------------------

def contact(request):

     if request.method=='POST':

        fname= request.POST['fname']
        lname = request.POST['lname']
        Email = request.POST['mail']
        phone = request.POST['phone']
        query = request.POST['query']
        
        contact_data=Query.objects.create(first_name=fname,last_name=lname,Email=Email,phone=phone,query=query)
        contact_data.save()
        messages.info(request,'Your Queries have been submitted successfully')
        return render(request,"blog/blog-contact.html")

     else:
      return render(request,"blog/blog-contact.html")

# ------------------------------------------------------------------------------------------------------------------------------------------------

def blogpost(request,slug):

    blog=BlogModel.objects.filter(slug=slug).first()
    context={'blog':blog}         
    return render(request,"blog/blog-post.html",context)

# ------------------------------------------------------------------------------------------------------------------------------------------------

def landing(request):

    return render(request,"blog/blog-landing.html")

# ------------------------------------------------------------------------------------------------------------------------------------------------

def signin(request):

    if request.method=='POST':
        username= request.POST['username']
        password= request.POST['password']
             
        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return render (request,"blog/blog-home.html")
        else:
            messages.info(request,'Invalid Credentials')
            return render(request,"blog/blog-login.html") 
    else:
        return render(request,"blog/blog-login.html")       

# ------------------------------------------------------------------------------------------------------------------------------------------------

def signout(request):

        logout(request)
        return redirect('landing-page')
        

# ------------------------------------------------------------------------------------------------------------------------------------------------

def Register(request):

    if request.method=='POST':

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        # terms_conditions=request.POST.get('terms_conditions','off')

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username already exists')
                return render(request,"blog/blog-Register.html")
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email already exists')
                return render(request,"blog/blog-Register.html")
           
            else:
                user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password1)
                user.save()
                messages.info(request,'You have been Successfully registered')
                return render (request,"blog/blog-login.html")

        else:
            messages.info(request,"Passwords Do not match")
            return render(request,"blog/blog-Register.html")      


    else:
        return render(request,"blog/blog-Register.html")

# ------------------------------------------------------------------------------------------------------------------------------------------------

def Myblogs(request):

    no_of_posts = 2

    page=request.GET.get('page')

    if page is None:
        page=1
    else:
        page=int(page)
    
    myblogs=BlogModel.objects.filter(author=request.user)
    length=len(myblogs)
    myblogs=myblogs[(page-1)*no_of_posts: page*no_of_posts]

    if page > 1:

        prev=page-1

    else:

        prev=None

    if page < math.ceil(length/no_of_posts):

        next=page+1

    else:

        next=None

    context={'myblogs':myblogs,'prev':prev,'next':next,}
    return render(request,"blog/blog-self.html",context)

#---------------------------------------------------------------------------------------------------------------------------------------------------


def delete_view(request,slug):
    
    blog=BlogModel.objects.filter(slug=slug).first()
    context={'blog':blog}         
    return render(request,"blog/delete_view.html",context)
    
def delete(request,slug):
    blog = blog=BlogModel.objects.filter(slug=slug).first()
    blog.delete()
    return redirect('Myblogs')

# ------------------------------------------------------------------------------------------------------------------------------------------------------
# This view function is currently bugged and is not working.. 

def update_view(request, slug):

    obj = get_object_or_404(BlogModel, slug = slug)

    form = BlogForm(request.POST or None, instance = obj)
    context={'form':form}

    if form.is_valid():
        obj=form.save(commit=False)
        obj.save()
        context={'form':form}
        return render (request,'blog/update_views.html',context)
    else:
        context = {'form':form}
        return render (request,'blog/update_views.html',context)
 
   
   
 
    