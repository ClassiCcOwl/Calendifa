from rest_framework import serializers
from django.utils import timezone


class CustomResponseSerializer(serializers.Serializer):
    now = serializers.SerializerMethodField()
    day = serializers.IntegerField(min_value=1, max_value=31)
    date = serializers.CharField()
    time = serializers.CharField()
    month = serializers.IntegerField(min_value=1, max_value=12)
    year = serializers.IntegerField(min_value=1000)
    timestamp = serializers.FloatField()
    hour = serializers.IntegerField(min_value=0, max_value=23)
    minute = serializers.IntegerField(min_value=0, max_value=59)
    second = serializers.IntegerField(min_value=0, max_value=59)
    week_of_year = serializers.IntegerField(min_value=1, max_value=53)
    day_of_week = serializers.IntegerField(min_value=1, max_value=7)
    utc = serializers.CharField()
    status_code = serializers.IntegerField(min_value=100, max_value=599)
    date = serializers.CharField()

    def get_now(self, obj):
        return timezone.now().strftime('%A %d %B %Y %H:%M:%S')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["utc"] = timezone.now().isoformat()
        return data
