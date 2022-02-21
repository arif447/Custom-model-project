from django.urls import path
from Custom_model import views
app_name = 'Custom_model'


urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('', views.index, name='index'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('employee/', views.Employee, name='employee'),
    path('staff/', views.Staff, name='staff'),

]

