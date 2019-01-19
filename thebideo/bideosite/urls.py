from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('podcast/', views.podcast, name='podcast'),
    # path('comment/', views.comment, name='comment'),
    path('reviews/', views.reviews, name='reviews'),
]
