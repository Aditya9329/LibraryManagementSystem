from django.urls import path
from .import views

urlpatterns = [
    path('',views.base,name="base"),
    path('student_registor',views.student_registor,name="student_registor"),
    path('find_books',views.find_books,name="find_books"),
    path('available_books',views.available_books,name="available_books"),
  
]


# path('',views.home,name="home"),
# path('signup',views.signup,name='signup'),