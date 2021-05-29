from django.urls import path
from . import views
from django.conf.urls import url, include
from usersnips import views as usersnips_views

extra_patterns = [
    path('snippet_detail/', usersnips_views.snippet_detail),
]


urlpatterns = [
   path('', views.home, name="home"),
   path('login/', views.login_user, name='login'),
   path('logout/', views.logout_user, name='logout'),
   path('register/', views.register_user, name='register'),
   path('edit_profile/', views.edit_profile, name='edit_profile'),
   path('change_password', views.change_password, name='change_password'),
   path('new_profile_home', views.new_profile_home, name='new_profile_home'),
   path('returning_profile_home', views.returning_profile_home, name='returning_profile_home'),
]
