from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('accounts/', include('accounts.urls')),
    path('news/', views.news_view),
    path('hikes/', views.hikes_view),
    path('about/', views.about_view),
    path('contacts/', views.contacts_view),
]