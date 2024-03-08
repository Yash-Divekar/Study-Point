from django.urls import path
from . import views

urlpatterns=[
    path('',views.homepage,name='homepage'),
    path('login',views.login_user, name='login'),
    path('signup',views.signup_user,name='signup'),
    path('logout',views.logout_user,name='logout'),
    path('home',views.home,name='home'),
    path('exam',views.exam,name='exam'),
    path('get-nested-dictionary/',views.get_nested_dictionary,name='get_nested_dictionary'),
    path('syllabus',views.syllabus,name='syllabus'),
    path('add',views.add,name='add'),
    path('tan',views.tan,name='tan'),
]