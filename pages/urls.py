from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page, name='home'),
    path('contact/', views.contact_page, name='contact'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('cookie_consent/', views.cookie_consent_view, name='cookie_consent'),
    path('<path:slug>/', views.general_page, name='general_page'),
]