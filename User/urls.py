from django.urls import path
from . import views
from .views import ProfileDetailView

app_name = 'User'
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('send_mail/', views.mail, name='send_mail'),
    path('profile/', views.profile, name='profile'),
    path('profile_detail/<int:pk>/', ProfileDetailView.as_view(), name='profile_detail'),
    path('profile_edit', views.profile_edit, name='profile_edit'),
]

