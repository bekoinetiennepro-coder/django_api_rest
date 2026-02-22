from api.models import Product
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    author_products = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'author_products']
        
    def get_author_products(self, obj):
        products = obj.product_set.all()  
        context = self.context  
        return ProductSerializer2(products, many=True, context=context).data
        
        
class ProductSerializer1(serializers.ModelSerializer):
    email = serializers.EmailField(write_only=True)
    price_in_errors = serializers.SerializerMethodField()
    description_in_erros = serializers.SerializerMethodField()
   # detail_link= serializers.CharField(source='get_absolute_url', read_only=True)
    link = serializers.HyperlinkedIdentityField(view_name='api:product_api_view_detail', lookup_field='pk')
    author = UserSerializer()
    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']
    
    def create(self, validated_data):
        email = validated_data.pop('email')
        print(f"Email reçu : {email}")
        user = self.context['request'].user
        validated_data['author'] = user
        return super().create(validated_data)
        
    def get_price_in_errors(self, obj):
        return obj.get_price_in_erros()
        
    def get_description_in_erros(self, obj):
        return obj.get_description_short()
    
    # def get_detail_link(self, obj):
    #    return obj.get_absolute_url()
        
class ProductSerializer2(serializers.ModelSerializer):
    link = serializers.HyperlinkedIdentityField(view_name='api:product_api_view_detail', lookup_field='pk')
    class Meta:
       model = Product
       fields = ['id', 'name', 'price', 'description', 'link']