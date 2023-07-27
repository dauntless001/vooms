from django.urls import path
from student import views

app_name = 'student'

urlpatterns = [
    path("", views.StudentsView.as_view(), name='students'),
    path("add-student/", views.CreateStudent.as_view(), name='add-student'),
    path("colleges/", views.CollegeListView.as_view(), name="colleges"),
    path("colleges/<int:college_id>/", views.CollegeDetailView.as_view(), name="college-detail"),
    path("colleges/<int:college_id>/<int:programme_id>/", views.StudentsByProgrammeView.as_view(), name="programme-students"),
    path("<str:slug>/", views.StudentDetail.as_view(), name='student-detail'),
    path("<str:slug>/verify/", views.VerifyStudent.as_view(), name='student-verify'),
    path("<str:slug>/edit/", views.UpdateStudent.as_view(), name='student-edit'),
    path("<str:slug>/delete/", views.DeleteStudent.as_view(), name='student-delete'),
    path("<str:slug>/document/<str:doc_slug>/delete/", views.DeleteDocument.as_view(), name='delete-student-document'),
]