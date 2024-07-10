from rest_framework import serializers
from .models import Analyze, Market, Chat

class AnalyzeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Analyze
        fields = '__all__'

class MarketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Market
        fields = '__all__'

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = '__all__'