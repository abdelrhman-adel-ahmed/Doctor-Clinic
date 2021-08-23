from core.models import *
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *

# project level permission is applied with allowany


@api_view(["GET"])
def api(request):
    api_url = {
        "list-Doc-Reservation": "doctor-appointment/<int:pk>",
        "list-Patient-Reservation": "patient-appointment/<int:pk>",
        "Register": "/register",
        "Make-Reservation": "reservation",
        "Update-Reservation": "manage-reservation/<int:pk>",
        "Delete-Reservation": "delete-reservation/<int:pk>",
        "List-All-Reservations": "show-reservation",
    }
    return Response(api_url)


class RegisterUser(generics.CreateAPIView):
    serializer_class = RegisterSerlizer


class MakeReservation(generics.CreateAPIView):
    serializer_class = ReservationSerializer


class ShowPatientReservation(APIView):
    def get(self, request, pk):
        pat = get_object_or_404(Patient, pk=pk)
        print(pat)
        data = Reservation.objects.filter(patient=pat)
        patient_reservations = ReservationSerializer(data, many=True)
        return Response(patient_reservations.data)


class ShowDoctorAppointmnet(APIView):
    def get(self, request, pk):
        doc = get_object_or_404(Doctor, pk=pk)
        print(doc)
        clinics = doc.get_doctor_clincs
        data = Reservation.objects.filter(clinic__in=clinics)
        doc_reservations = ReservationSerializer(data, many=True)
        return Response(doc_reservations.data)


class ListReservation(generics.ListAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


class ReservationUpdate(generics.RetrieveUpdateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


class ReservationDelete(generics.RetrieveDestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
