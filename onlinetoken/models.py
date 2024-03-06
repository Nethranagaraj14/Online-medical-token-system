from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Hospital(models.Model):
    hid = models.BigIntegerField()
    hname = models.CharField(max_length = 50)
    street = models.CharField(max_length = 50)
    city = models.CharField(max_length = 50)
    state = models.CharField(max_length = 50)
    pincode = models.IntegerField()
    contact = models.IntegerField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    # rid = models.ForeignKey('Review',on_delete = models.CASCADE)
    image = models.CharField(max_length = 600)

class Department(models.Model):
    did = models.BigIntegerField()
    dname = models.CharField(max_length = 50)
    noOfDoc = models.IntegerField()
    block = models.CharField(max_length = 50)
    noOfBeds = models.IntegerField()
    hid = models.ForeignKey('Hospital',on_delete = models.CASCADE)
    image = models.CharField(max_length = 600)

class Review(models.Model):
    rid = models.BigIntegerField()
    date = models.DateField()
    rating = models.IntegerField()
    content = models.CharField(max_length = 100)
    docid = models.ForeignKey('Doctordetails',on_delete = models.CASCADE)
    hid = models.ForeignKey('Hospital',on_delete = models.CASCADE)
    pid = models.ForeignKey('Patient',on_delete = models.CASCADE)


class Doctordetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    docid = models.BigIntegerField()
    contact = models.IntegerField()
    starting_time = models.TimeField()
    ending_time = models.TimeField()
    mnoOfToken = models.IntegerField()
    anoOfToken = models.IntegerField(default=0)
    enoOfToken = models.IntegerField()
    period = models.CharField(max_length = 20)
    # rid = models.ForeignKey('Review',on_delete = models.CASCADE)
    did = models.ForeignKey('Department',on_delete = models.CASCADE)
    hid = models.ForeignKey('Hospital',on_delete = models.CASCADE)
    study = models.CharField(max_length = 20)


class Patient(models.Model):
    pid = models.BigIntegerField()
    contact = models.IntegerField()
    reason = models.CharField(max_length = 100)
    status = models.CharField(max_length = 20)
    street = models.CharField(max_length = 20)
    city = models.CharField(max_length = 20)
    state = models.CharField(max_length = 20)
    date = models.DateField()
    # rid = models.ForeignKey('Review',on_delete = models.CASCADE)
    did = models.ForeignKey('Department',on_delete = models.CASCADE)
    hid = models.ForeignKey('Hospital',on_delete = models.CASCADE)
    docid = models.ForeignKey('Doctordetails',on_delete = models.CASCADE)
    
# chatgpt code

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctordetails, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)

    accepted = models.BooleanField(default=False)
    status = models.CharField(max_length=50, choices=[("pending","Pending"),("accepted","Accepted"),("declined","Declined")]) # Add a status field
