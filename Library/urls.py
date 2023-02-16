from django.urls import path
from .import views

urlpatterns = [
    path('',views.base,name="base"),
    path('student_registor',views.student_registor,name="student_registor"),
]


# path('',views.home,name="home"),
# path('signup',views.signup,name='signup'),