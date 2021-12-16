from django.urls import path
from app import views as v

urlpatterns = [
    path('', v.home,name='home'),
    path('login/', v.login,name='login'),
    path('signup/', v.signup,name='signup'),
    path('dashboard/', v.dashboard,name='dashboard'),
    path('about/', v.about,name='about'),
    path('contact/', v.contact,name='contact'),
    path('logout/',v.logout, name='logout'),
  
    path('mypost/', v.mypost,name='mypost'),
    path('mypost/<pk>/', v.detail_view,name='detail'),
    path('mypost/delete/<pk>/', v.delete_view,name='delete'),
    
]
