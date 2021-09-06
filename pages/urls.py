from django.urls import path
from django.urls.resolvers import URLPattern
from .views import HomePageView, AboutPageView

urlpatterns = [
    # path('', HomePageView, name='home'),
    path('about', AboutPageView.as_view(), name='about'),   
    path('', HomePageView.as_view(), name='home'),   
]