from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('',views.index,name="index"),
    path('library', views.home,name="home"),
    path('about/',views.about,name="about"),
    path('contact', views.contact,name="contact"),
    path('library/admin', views.admin,name='libadmin'),
    path('library/student', views.student, name="student"),
    path('library/adminsignup', views.adminsignup,name="adminsignup"),
    path('library/studentsignup', views.studentsignup,name="studentsignup"),
    path('library/adminlogin', LoginView.as_view(template_name='adminlogin.html')),
    path('library/studentlogin', LoginView.as_view(template_name='studentlogin.html')),
    path('logout', LogoutView.as_view(template_name='home.html')),
    path('afterlogin', views.afterlogin,name="afterlogin"),
    path('addbook', views.addbook,name="addbook"),
    path('viewbook', views.viewbook,name="viewbook"),
    path('viewbookstudent',views.viewbookstudent,name="viewsbookstudent"),
    path('issuebook', views.issuebook,name="issuebook"),
    path('viewissuedbook', views.viewissuedbook,name="viewissuedbook"),
    path('viewstudent', views.viewstudent,name="viewstudent"),
    path('viewissuedbookbystudent', views.viewissuedbookbystudent,name="viewissuedbookbystudent"),
    
   
]
