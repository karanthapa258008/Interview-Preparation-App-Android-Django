from django.urls import path
from . import views

urlpatterns = [

    # MCQ APIs
    path('Java/', views.getJavaQuestions),
    path('Python/', views.getPythonQuestions),
    path('JS/', views.getJsQuestions),
    path('c++/', views.getcQuestions),
    path('sql/', views.getsqlQuestions),
    path('css/', views.getcssQuestions),
    path('html/', views.gethtmlQuestions),

    # Interview APIs
    path('InterviewJava/', views.getJavaInterview),
    path('InterviewPython/', views.getPythonInterview),
    path('InterviewJS/', views.getJsInterview),
    path('Interviewc/', views.getcInterview),
    path('Interviewsql/', views.getsqlInterview),
    path('Interviewhtml/', views.gethtmlInterview),
    path('Interviewcss/', views.getcssInterview),

    path('ApptitudeJava/', views.getJavaApptitude),
    path('ApptitudePython/', views.getPythonApptitude),
    path('ApptitudeJS/', views.getJsApptitude),
    path('Apptitudecss/', views.getcssApptitude),
    path('Apptitudesql/', views.getsqlApptitude),
    path('Apptitudehtml/', views.gethtmlApptitude),
     path('Apptitudecp/', views.getcpApptitude),

    path("send-otp/", views.send_otp),
    path("verify-otp/", views.verify_otp),
    path("login/", views.login_user),
]