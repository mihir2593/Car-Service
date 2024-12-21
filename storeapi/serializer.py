from rest_framework import routers, serializers, viewsets
from storesapp import models

class categoryserializer(serializers.ModelSerializer):
    class Meta:
        model = models.categorymodel
        fields = "__all__"



class usecategoryserializer(serializers.ModelSerializer):
    class Meta:
        model = models.usecategorymodel
        fields = "__all__"


class productserializer(serializers.ModelSerializer):
    class Meta:
        model = models.productmodel
        fields = "__all__"


class storeserializer(serializers.ModelSerializer):
    class Meta:
        model = models.storemodel
        fields = "__all__"