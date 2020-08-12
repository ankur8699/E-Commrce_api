from rest_framework import serializers 
from .models import Products, Details,Images
        
class DetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Details
        fields = ('id','ids',)
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ('idi','img','img2','img3','img4','img5')        

class ProductsListSerializer(serializers.ModelSerializer):
    Images=ImageSerializer(read_only=True , many=True,)
    class Meta:
        model = Products
        fields = ('__all__')   

