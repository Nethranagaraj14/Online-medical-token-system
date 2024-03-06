from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('hospital/', views.hospital, name='hospital'),
    path('department/<int:hid>/', views.department, name='department'),
    path('doctor/<int:did>', views.doctor, name='doctor'),
    path('docdisplay/<int:pk>', views.docdisplay, name='docdisplay'),
    path('period/',views.period,name='period'),
    path('',views.home,name='home'),
    path('doctorpage/',views.doctorpage,name='doctorpage'),
    path('base/',views.base,name='base'),
    # path('doctor_detail/<int:aappointment_id>',views.doctor_detail,name='doctor_detail'),

    path('apply_token/<int:doctor_id>/', views.apply_token, name='apply_token'),
    path('doctor_detail/<int:doctor_id>/', views.doctor_detail, name='doctor_detail'),
    path('accept_appointment/<int:appointment_id>/', views.accept_appointment, name='accept_appointment'),
    path('decline_appointment/<int:appointment_id>/', views.decline_appointment, name='decline_appointment'),
    # path('doctorvisible/',views.doctorvisible,name='doctorvisible'),
    # path('patient_status/<int:patient_id>/', views.patient_status, name='patient_status'),

    path('patient_status/<int:patient_id>/', views.patient_status, name='patient_status'),

    path('register/', views.registerpage, name='registerpage'),
    path('login/', views.loginpage, name='loginpage'),
    path('logout/', views.logoutUser, name='logoutpage'),

    # Add other URLs as needed
    path('appoitnment_success/', views.appointment_success, name='appointment_success'),
    path('apply_appointment/', views.apply_appointment, name='apply_appointment'),


]


