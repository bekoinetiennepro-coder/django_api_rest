from api.models import Product
from rest_framework import serializers

class ProductSerializer1(serializers.ModelSerializer):
    email = serializers.EmailField(write_only=True)
    price_in_errors = serializers.SerializerMethodField()
    description_in_erros = serializers.SerializerMethodField()
   # detail_link= serializers.CharField(source='get_absolute_url', read_only=True)
    link = serializers.HyperlinkedIdentityField(view_name='api:product_api_view_detail', lookup_field='pk')
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'created_at', 'update_at', 'email', 'price_in_errors', 'description_in_erros', 'link']
        read_only_fields = ['id', 'created_at', 'updated_at']
    
    def create(self, validated_data):
        email = validated_data.pop('email')
        print(f"Email reçu : {email}")
        return super().create(validated_data)
        
    def get_price_in_errors(self, obj):
        return obj.get_price_in_erros()
        
    def get_description_in_erros(self, obj):
        return obj.get_description_short()
    
    # def get_detail_link(self, obj):
    #    return obj.get_absolute_url()
        
class ProductSerializer2(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    price = serializers.FloatField()
    description = serializers.CharField(max_length=500, required=False, allow_blank=True)
    
    