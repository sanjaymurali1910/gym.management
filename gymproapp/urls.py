from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('About/',views.About,name='About'),
    path('Services/',views.Services,name='Services'),
    path('tutorial/',views.tutorial,name='tutorial'),
    path('add_contact/',views.add_contact,name='add_contact'),
    path('view_contact',views.view_contact,name='view_contact'),
    path('admin_login',views.admin_login,name='admin_login'),
    path('admin_homepage/',views.admin_homepage,name='admin_homepage'),
    path('admin_logout',views.admin_logout,name='admin_logout'),
    path('add_plan',views.add_plan,name='add_plan'),
    path('view_plan',views.view_plan,name='view_plan'),
    path('add_equipments/',views.add_equipments,name='add_equipments'),
    path('view_equipments/',views.view_equipments,name='view_equipments'),
    path('view_equipments/delete_equipments/',views.delete_equipments,name='delete_equipments'),
    path('delete_plan/',views.delete_plan,name='delete_plan'),
    path('delete_contact/',views.delete_contact,name='delete_contact'),
    path('add_member/',views.add_member,name='add_member'),
    path('view_member/',views.view_member,name='view_member'),
    path('view_member/delete_member',views.delete_member,name='delete_member'),
]