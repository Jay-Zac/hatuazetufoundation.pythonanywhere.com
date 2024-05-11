from django.urls import path
from . import views

app_name = 'homepage'
urlpatterns = [
    path('', views.home_page_view, name='index'),
    path('engagements/', views.engagements_view, name='strategic_engagements'),
    path('<int:pk>/', views.detail_view, name='detail'),

]
