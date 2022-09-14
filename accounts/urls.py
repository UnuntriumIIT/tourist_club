from django.urls import path
from tourist_site.views import login_view, logout_view, profile_view, register_view

urlpatterns = [
    path('login/', login_view),
    path('registration/', register_view),
    path('logout/', logout_view),
    path('profile/', profile_view),
]