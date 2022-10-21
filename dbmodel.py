from django.db import models

class Appointments(models.Model):
    # patient_id = models.CharField(max_length = 200)
    Patient_name = models.CharField(max_length = 200)
    gender = models.CharField(max_length = 100)
    patient_age = models.IntegerField()
    disease = models.CharField(max_length = 200)
    date_time = models.FloatField()
    contact = models.CharField(max_length=200)
    doctor_name = models.CharField(max_length = 200)
    department = models.CharField(max_length = 200)
    doctor_id = models.CharField(max_length = 200)

    class Meta:
        db_table = "appointment_info"

class Doctors(models.Model):
    doctor_name = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    doctor_id = models.CharField(max_length=200)

    class Meta:
        db_table = "doctors_info"

