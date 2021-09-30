from django.urls import path
from . import views




urlpatterns = [  
    path('' , views.landing , name='landing-page'),
    path('Login/' , views.signin , name='login-page'),
    path('Register/' , views.Register , name='Register-page'),
    path('home/' , views.home , name='Home-page'),
    path('signout/' , views.signout , name='sign-out'),
    path('blogpost/<str:slug>' , views.blogpost , name='blogpost'),
    path('blog/' , views.blog , name='blog'),
    path('search/' , views.search , name='search'),
    path('contact/' , views.contact , name='contact'),
    path('create/' , views.create , name='create'),
    path('Myblogs/' , views.Myblogs , name='Myblogs'),
    path('delete/<str:slug>' , views.delete , name='deletepost'),
    path('deleteview/<str:slug>', views.delete_view , name='deleteview'),
    path('update/<str:slug>', views.update_view , name= 'updateview'),
    
]
 