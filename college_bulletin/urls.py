# collegebulletin/urls.py
from django.contrib import admin
from django.urls import path
from miniproject import views as miniproject_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('logout/', miniproject_views.custom_logout, name='custom_logout'),
    path('home/',miniproject_views.home,name="home"),
    path('signup/',miniproject_views.signup,name="signup"),
    path("home/chat/", miniproject_views.rooms, name="rooms"),
    path('login/', miniproject_views.login_view, name='login'),
    path('home/add_event/', miniproject_views.add_event, name='add_event'),
    path('calendar/', miniproject_views.calendar, name='calendar'),
    path('calendar.html/', miniproject_views.calendar, name='calendar_html'),
    path('home/placements/', miniproject_views.placement_list, name='placement-list'),
    path('miniproject/signup/', miniproject_views.signup, name='signup'),  # New path for signup
    path("<str:slug>/", miniproject_views.room, name='room'),
   
]
