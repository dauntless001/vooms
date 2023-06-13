from django.urls import path
from home import views

app_name = 'home'

urlpatterns = [
    path("", views.IndexView.as_view(), name='index'),
    path("about-us/", views.AboutUs.as_view(), name='about-us'),
    path("get-in-touch/", views.ContactUs.as_view(), name='get-in-touch'),
    path("dashboard/", views.DashboardView.as_view(), name='dashboard'),
    path("edit-profile/", views.EditProfile.as_view(), name='edit-profile'),
    path("create-student-profile/", views.CreateProfile.as_view(), name='student-profile'),
]