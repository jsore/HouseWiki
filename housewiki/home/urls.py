"""
…/HouseWiki/housewiki/home/urls.py
"""


from django.urls import path
from . import views


# define this app's namespace
app_name = 'housewiki'


# POST views
urlpatterns = [

    # path takes no args and is mapped to 'dashboard' view
    path('', views.dashboard, name='dashboard'),
]
