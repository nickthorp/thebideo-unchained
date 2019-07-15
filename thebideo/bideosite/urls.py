from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('podcast/', views.podcast, name='podcast'),
    path('healthz', views.healthz, name='healthz'),
    path('reviews/', views.reviews, name='reviews'),
    path('updatePodcasts/', views.update_podcasts, name='update_podcasts'),
]
