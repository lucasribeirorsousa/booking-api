from rest_framework import serializers
from .models import Reservation


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'
    

    def validate(self, data):
        if data['check_in'] > data['check_out']:
            raise serializers.ValidationError("start date can not be after end date")
        return data