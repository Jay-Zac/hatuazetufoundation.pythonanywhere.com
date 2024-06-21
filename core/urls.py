from django.urls import path
from . import views

app_name = 'core'
urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('engagements/', views.engagements_view, name='strategic_engagements'),
    path('<int:pk>/', views.detail_view, name='detail'),

]
