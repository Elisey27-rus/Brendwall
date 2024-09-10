from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price']

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Введите корректные данные")
        return value

    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Пустая строка")
        return value
