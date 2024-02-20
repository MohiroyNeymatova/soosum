from rest_framework import serializers
from .models import *


class MainBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainBanner
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = ['id', 'old_price', 'new_price', 'profit']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'image', 'name', 'price']


class InfoAboutProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfoAboutProduct
        fields = "__all__"


class AboutCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutCompany
        fields = "__all__"


class DiseaseBannerSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = DiseaseBanner
        fields = "__all__"


class HowToUseSerializer(serializers.ModelSerializer):
    class Meta:
        model = HowToUse
        fields = "__all__"


class NumberFactSerializer(serializers.ModelSerializer):
    class Meta:
        model = NumberFact
        fields = "__all__"


class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = "__all__"


class LogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = ['logo']
