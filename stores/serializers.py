from rest_framework import serializers
from .models import Stores


class StoresSerializers(serializers.ModelSerializer):
    class Meta:
        model = Stores
        fields = "__all__"
        read_only_fields = ["__all__"]
