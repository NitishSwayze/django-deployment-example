from django.urls import path
from AppThree import views

# TEMPLATE TAGGING
app_name = 'AppThree'

urlpatterns = [
    path('relative/', views.relative, name='relative'),
    path('visitor/', views.visitor, name='visitor_page'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='user_login')
]
