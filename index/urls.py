from django.urls import path
from.import views

urlpatterns = [
path('',views.index,name="in"),
path('about',views.about,name="ab"),
path('cour/',views.courses,name="courses"),
path('contact/',views.contact,name="cont"),
path("int:pk",views.coursescat,name="col")
]