from rest_framework import serializers
from .models import Career

class CareerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Career
        fields = '__all__'
        read_only_fields = ['id']

    def update(self, instance, validated_data):
        request = self.context.get('request')

        if request and request.method == 'PATCH':
            for field in ['username', 'created_datetime']:
                if field in validated_data:
                    raise serializers.ValidationError({field: f"The field '{field}' can not updated."})
                
        return super().update(instance, validated_data)