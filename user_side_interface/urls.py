from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),

    path('dash/', views.dashboard, name="dash"),
    path('profile/', views.user_profile, name="profile"),
    path('application/', views.application, name="application"),
    path('track_application/', views.track_application, name="track_application"),

    path('logout/', views.logout_view, name="logout"),

]