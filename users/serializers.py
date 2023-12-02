from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        optional_fields = ['first_name', 'last_name']
        data = {}
        for field in optional_fields:
            if field in validated_data:
                data[field] = validated_data[field]
            else:
                data[field] = ''
        user = User.objects.create(
            email=validated_data['email'],
            first_name=data['first_name'],
            last_name=data['last_name'],
        )
        user.set_password(validated_data['password'])
        user.is_active = False
        user.save()

        return user

    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ('last_login', 'is_superuser', 'is_staff', 'is_active',
                            'date_joined', 'groups', 'user_permissions')
        write_only_fields = ('password', )
