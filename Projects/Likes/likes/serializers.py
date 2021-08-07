from rest_framework import serializers
from .models import *

class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = '__all__'
class QuoteUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuoteUser
        fields = '__all__'