from stockapp.models import Kospi
from rest_framework import serializers


class KospiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kospi
        fields = '__all__'