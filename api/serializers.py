from rest_framework.serializers import ModelSerializer
from .models import Center
from django.db.models import fields


class CenterSerialzer(ModelSerializer):
    class Meta:
        model=Center
        fields=["id","ide","name","address","district","test_type","lab_type","latitude","longitude"]
