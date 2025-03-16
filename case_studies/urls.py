from django.urls import path
from . import views


urlpatterns = [
    path('<slug:parent_slug>/case-studies/<slug:slug>/', views.case_study_detail, name='case_study_detail'),
]