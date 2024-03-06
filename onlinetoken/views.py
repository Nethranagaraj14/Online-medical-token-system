from django.shortcuts import render,redirect
from . models import *
from django.contrib.auth.models import User,Group
from django.shortcuts import get_object_or_404

from .decoraters import *
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import UserCreationForm 
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth import get_user_model


User = get_user_model()

# Create your views here.

def hospital(request):
    hospital_objects = Hospital.objects.all()
    return render(request, 'hospital.html', {'hospital_objects':hospital_objects})     

def department(request,hid):
    hospital = get_object_or_404(Hospital, hid=hid)
    departments_in_hospital = Department.objects.filter(hid=hospital)
    department_objects = Department.objects.all()
    return render(request, 'department.html',{'department_objects':department_objects,'departments_in_hospital':departments_in_hospital,'hospital':hospital})

def doctor(request,did):
    department = get_object_or_404(Department, did=did)
    doctors_in_department = Doctordetails.objects.filter(did=department)
    doctor_objects = Doctordetails.objects.all()
    # user_objects = User.objects.all()
    return render(request, 'doctor.html',{'doctor_objects':doctor_objects,'doctors': doctors_in_department, 'department': department})
@login_required(login_url='login/')
def docdisplay(request,pk):
    item = Doctordetails.objects.get(pk=pk)
    user = item.user # Retrieve the associated user object
    return render(request,'docdisplay.html',{'item':item,'user':user})

def period(request):
    # hospital_id = 1  # Replace with the ID of the selected hospital
    # department_id = 1  # Replace with the ID of the selected department
    # doctor_id = 1  
    # doctor_id = get_object_or_404(Doctordetails,pk)
    # department_id = Department.objects.filter(pk=doctor_id)
    # hospital_id = Hospital.objects.filter(pk=department_id)
    return render(request,'period.html')

def home(request):
    user = request.user
    # doctor = Doctordetails.objects.get(pk=doctor_id)

    
    # To check and redirect the developer to doctor's page
    if request.user.groups.filter(name='Doctor').exists():
        appointment = Appointment.objects.filter(doctor__user=user).first()
        if appointment:
            return redirect('doctor_detail', doctor_id=appointment.doctor_id)



    # To check and redirect the admin to admin_dashboard page
    # if request.user.groups.filter(name='Admin').exists():
    #     return redirect('admin_dashboard')
    
    # To add every new user to general group
    patient_group = Group.objects.get(name='Patient')
    user.groups.add(patient_group)

    return render(request,'home.html')

def doctorpage(request):
    return render(request,'doctorpage.html')

def base(request):
    return render(request,'base.html')

#chatgpt
@doctor_required
def apply_token(request, doctor_id):
    if request.method == 'POST':
        # Assuming you have a form for applying token
        patient = request.user.patient
        doctor = Doctordetails.objects.get(pk=doctor_id)
        appointment = Appointment.objects.create(patient=patient, doctor=doctor)
        return redirect('doctor_detail', doctor_id=doctor_id)
    return render(request, 'apply_token.html',{'appointment':appointment})

@doctor_required
def doctor_detail(request, doctor_id):
    doctor = Doctordetails.objects.get(pk=doctor_id)
    appointments = Appointment.objects.filter(doctor=doctor)
    return render(request, 'doctor_detail.html', {'doctor': doctor, 'appointments': appointments})

# def accept_appointment(request, appointment_id):
#     appointment = Appointment.objects.get(pk=appointment_id)
#     appointment.accepted = True
#     appointment.save()

@doctor_required
def accept_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    appointment.accepted = True
    appointment.status = 'accepted'
    appointment.save()
    return redirect('doctor_detail',doctor_id=appointment.doctor_id)


# def decline_appointment(request, appointment_id):
#     appointment = Appointment.objects.get(pk=appointment_id)
#     appointment.accepted = False
#     appointment.save()
@doctor_required
def decline_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    appointment.accepted = False
    appointment.status = 'declined'
    appointment.save()
    return redirect('doctor_detail',doctor_id=appointment.doctor_id)


# def doctorvisible(request):
#     return render(request,'doctorvisible.html')


# def patient_status(request):
#     # Get the current user's appointment status
#     appointment = Appointment.objects.filter(patient=request.user.patient).first()
#     if appointment:
#         if appointment.accepted:
#             appointment_status = "Accepted"
#         else:
#             appointment_status = "Declined"
#     else:
#         appointment_status = "Pending"
    
#     return render(request, 'patient_status.html', {'appointment_status': appointment_status})



# def patient_status(request,patient_id):
#     # Assuming you have a way to identify the current patient, such as a session variable or a custom authentication mechanism
#     # For demonstration purposes, let's assume you have a session variable called 'patient_id'
#     patient_id = request.session.get('patient_id')
#     if patient_id:
#         patient = Patient.objects.get(pk=patient_id)
#         appointment = Appointment.objects.filter(patient=patient).first()
#         if appointment:
#             if appointment.accepted:
#                 appointment_status = "Accepted"
#             else:
#                 appointment_status = "Declined"
#         else:
#             appointment_status = "Pending"
    
#         return render(request, 'patient_status.html', {'appointment_status': appointment_status})
    
    # else:
        # return redirect('login_page')  # Redirect to login page if patient is not authenticated

# def patient_status(request):
#     # Get the current user's appointment status
#     appointment = Appointment.objects.filter(patient=request.user.patient).first()
#     if appointment:
#         if appointment.accepted:
#             appointment_status = "Accepted"
#         else:
#             appointment_status = "Declined"
#     else:
#         appointment_status = "Pending"
    
#     return render(request, 'patient_status.html', {'appointment_status': appointment_status})
    
def patient_status(request, patient_id):
    # Get the appointment status for the specified patient ID
    appointment = Appointment.objects.filter(patient_id=patient_id).first()
    if appointment:
        appointment_status = appointment.status
    else:
        appointment_status = "Pending"
    
    return render(request, 'patient_status.html', {'appointment_status': appointment_status})


# def patient_status(request, patient_id):
#     appointment = Appointment.objects.filter(patient_id=patient_id).first()
#     if appointment:
#         if appointment.accepted:
#             appointment_status = "Accepted"
#         else:
#             appointment_status = "Declined" if appointment.status == "Declined" else "Pending"
#     else:
#         appointment_status = "Pending"
    
#     return render(request, 'patient_status.html', {'appointment_status': appointment_status})

# Create your views here.

def registerpage(request):
    form=CreateUserForm()

    if request.method == 'POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request, 'Account was created for '+user)
            return redirect('loginpage')
    context={'form':form}
    return render(request,'registerpage.html',context)

def loginpage(request):

    if request.method == 'POST':
        username=request.POST.get('username')
        password= request.POST.get('password')

        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request, 'Username or password is incorrect')
    context={}
    return render(request,'loginpage.html',context)

def logoutUser(request):
    logout(request)
    return redirect('loginpage')


def apply_appointment(request):
    if request.method == 'POST':
        # Assuming you have a form that contains the necessary fields for appointment submission
        # patient = request.user
        patient = Patient.objects.get(user=request.user)
        
        # patient = Appointment.objects.filter(patient__user=request.user)


        doctor_id = request.POST.get('doctor_id')  # Assuming the doctor's ID is included in the form
        department_id = request.POST.get('department_id')  # Assuming the department's ID is included in the form
        hospital_id = request.POST.get('hospital_id')  # Assuming the hospital's ID is included in the form

        # Retrieve the doctor, department, and hospital objects
        doctor = User.objects.get(id=doctor_id)
        department = Department.objects.get(id=department_id)
        hospital = Hospital.objects.get(id=hospital_id)

        # Create the appointment instance and save it to the database
        appointment = Appointment.objects.create(patient=patient, doctor=doctor, department=department, hospital=hospital)
        
        # Optionally, you can redirect the user to a success page or another page after applying for the appointment
        return redirect('appointment_success')  # Replace 'appointment_success' with the appropriate URL name
    else:
        # Handle GET requests if needed
        pass

def appointment_success(request):
    return render(request,'appointment_success.html')
