from datetime import datetime

from core.models import *
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class ReservationTest(APITestCase):
    """
    1-test view reservation for doctor endpoint
    2-test view reservation for patient endpoint
    3-test create reservation endpoint
    4-test update reservation
    5-test delete reservation
    """

    def setUp(self):
        self.doctor_data = Doctor.objects.create(username="doc1")
        self.patient_data = Patient.objects.create(username="pat1")
        self.clinic = Clinic.objects.create(
            doctor=self.doctor_data,
            name="clinc1",
            price="13",
        )
        self.create_reservation_data = {"patient": 2, "clinic": 1}
        self.reservation = Reservation.objects.create(patient=self.patient_data, clinic=self.clinic)

    def test_create_reservation_endpoint(self):
        """
        test create reservation
        """
        url = reverse("api:make_reservation")
        response = self.client.post(url, self.create_reservation_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_view_patient_reservation(self):
        """
        test list the patient reservations (if no doctor found --> return code 404)
        """
        url = reverse("api:patient_reservations", kwargs={"pk": 2})
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_view_doctor_reservation(self):
        """
        test list the doctor reservations (if no patient found --> return code 404)
        """
        url = reverse("api:doctor_reservations", kwargs={"pk": 1})
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_reservation(self):
        """
        test update reservation
        """
        url = reverse("api:reservation_update", kwargs={"pk": 2})
        self.updated_data = {"patient": 3, "clinic": 1}
        response = self.client.put(url, self.updated_data, format="json")
        # 404 because we done have patient 3
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_reservation(self):
        """
        test delete reservation
        """
        url = reverse("api:reservation_delete", kwargs={"pk": 1})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
