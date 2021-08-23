from core.models import *
from rest_framework import serializers


class RegisterSerlizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "type", "password"]


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ["patient", "clinic"]
