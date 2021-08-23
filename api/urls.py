from django.urls import path

from .views import *

app_name = "api"

urlpatterns = [
    path("", api, name="home"),
    # register
    path("register/", RegisterUser.as_view(), name="resgister"),
    # create reservation
    path("reservation/", MakeReservation.as_view(), name="make_reservation"),
    # list reservation for doctors or patient
    path("patient-appointment/<int:pk>/", ShowPatientReservation.as_view(), name="patient_reservations"),
    path("doctor-appointment/<int:pk>/", ShowDoctorAppointmnet.as_view(), name="doctor_reservations"),
    # list all reservation on the system
    path("show-reservation/", ListReservation.as_view(), name="list_reservations"),
    # update reservation
    path("manage-reservation/<int:pk>/", ReservationUpdate.as_view(), name="reservation_update"),
    # delete reservation
    path("delete-reservation/<int:pk>/", ReservationDelete.as_view(), name="reservation_delete"),
]
