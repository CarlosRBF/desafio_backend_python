from rest_framework import serializers
from .models import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = "__all__"
        read_only_fields = ["store"]

    def create(self, validated_data: dict) -> Transaction:
        return Transaction.objects.create(**validated_data)

    def update(self, instance: Transaction, validated_data: dict) -> Transaction:
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save
        return instance
