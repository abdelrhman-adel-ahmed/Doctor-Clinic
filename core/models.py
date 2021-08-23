from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):

    # enum for django instead of tuple choices
    class Types(models.TextChoices):
        DOCTOR = "DOCTOR", "Doctor"
        PATIENT = "PATIENT", "Patient"

    base_type = Types.PATIENT

    type = models.CharField(_("Type"), max_length=50, choices=Types.choices, default=base_type)


class DoctorManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.DOCTOR)


class Doctor(User):
    base_type = User.Types.DOCTOR
    objects = DoctorManager()

    class Meta:
        proxy = True

    @property
    def get_doctor_clincs(self):
        return Clinic.objects.filter(doctor=self)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.Types.DOCTOR
        return super().save(*args, **kwargs)


class Clinic(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    name = models.CharField(max_length=15)
    price = models.DecimalField(decimal_places=2, max_digits=4)
    date = models.DateTimeField(null=True)
    start_time = models.TimeField(null=True)
    end_time = models.TimeField(null=True)

    def __str__(self):
        return self.name


class PatientManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.PATIENT)


class Patient(User):
    base_type = User.Types.PATIENT
    objects = PatientManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.Types.PATIENT
        return super().save(*args, **kwargs)


class Reservation(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)

    def __str__(self):
        return self.pk
