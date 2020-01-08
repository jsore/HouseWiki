"""
…/HouseWiki/housewiki/home/urls.py
"""


from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views


# define this app's namespace
app_name = 'housewiki'


# POST views
urlpatterns = [

    # path takes no args and is mapped to 'dashboard' view
    path('', views.dashboard, name='dashboard'),
    # path('', include(views.dashboard, views.HousePicturesView), name='dashboard'),
    path('milestones/', views.milestones, name='milestones'),
    path('questions/', views.questions, name='questions'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('tips/', views.tips, name='tips'),
    path('otherfactors/', views.otherfactors, name='otherfactors'),
    # path('user/login/', views.user_login, name='login'),
    path('user/login/', auth_views.LoginView.as_view(), name='login'),
    path('user/logout/', auth_views.LogoutView.as_view(), name='logout'),
]
