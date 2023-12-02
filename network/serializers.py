from rest_framework import serializers

from network.models import Product, Company
from network.validators import CompanyLevelValidation


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    products_detail = ProductSerializer(many=True, read_only=True, source='products')

    class Meta:
        model = Company
        fields = ['id', 'network_type', 'level', 'title', 'email', 'country', 'city', 'street', 'house', 'products',
                  'products_detail', 'provider', 'debt', 'create_time']
        read_only_fields = ['debt', ]
        validators = [CompanyLevelValidation(), ]
