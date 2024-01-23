from django.urls import path
from . import views

urlpatterns = [
    path('reg/', views.reg, name='reg'),
    path('login/', views.login_page, name='login_page'),
    path('logout/', views.logout_page, name='logout'),
    path('notes/', views.notes, name='notes'),
    path('add_note/', views.add_note, name='add_note'),
]
