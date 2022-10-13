from operator import mod
from django.db import models

# Create your models here.
# Target model = ManyToManyField 가 없는 곳
class Patient(models.Model):
    name = models.TextField()
    # doctor = models.ManyToManyField(Doctor)

    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'

# Source
class Doctor(models.Model):
    name = models.TextField()
    patients = models.ManyToManyField(Patient, through='Reservation')

    def __str__(self):
        return f'{self.pk}번 의사 {self.name}'

class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    symptom = models.TextField()
    reserved_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.doctor.pk}번 의사-{self.patient.pk}번 환자'
