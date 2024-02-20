from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from .serializer import *
from rest_framework.response import Response

# http_method_names = ['get', 'post']


class MainBannerView(ReadOnlyModelViewSet):
    queryset = MainBanner.objects.all()
    serializer_class = MainBannerSerializer
    http_method_names = ['get']

    def list(self, request):
        queryset = self.queryset.last()
        ser = self.serializer_class(queryset)
        return Response(ser.data)


class OrderView(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    http_method_names = ['post']


class DiscountView(ModelViewSet):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer
    http_method_names = ['get']

    def list(self, request):
        queryset = self.queryset.last()
        ser = self.serializer_class(queryset)
        return Response(ser.data)


class ProductView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    http_method_names = ['get']

    def list(self, request):
        queryset = self.queryset.order_by('-id')[:2]
        ser = self.serializer_class(queryset, many=True)
        return Response(ser.data)


class InfoAboutProductView(ReadOnlyModelViewSet):
    queryset = InfoAboutProduct.objects.all()
    serializer_class = InfoAboutProductSerializer
    http_method_names = ['get']

    def list(self, request):
        queryset = self.queryset.order_by('-id')[:3]
        ser = self.serializer_class(queryset, many=True)
        return Response(ser.data)


class AboutCompanyView(ReadOnlyModelViewSet):
    queryset = AboutCompany.objects.all()
    serializer_class = AboutCompanySerializer
    http_method_names = ['get']

    def list(self, request):
        queryset = self.queryset.last()
        ser = self.serializer_class(queryset)
        return Response(ser.data)


class DiseaseBannerView(ReadOnlyModelViewSet):
    queryset = DiseaseBanner.objects.all()
    serializer_class = DiseaseBannerSerializer
    http_method_names = ['get']

    def list(self, request):
        queryset = self.queryset.last()
        ser = self.serializer_class(queryset)
        return Response(ser.data)


class HowToUseView(ReadOnlyModelViewSet):
    queryset = HowToUse.objects.all()
    serializer_class = HowToUseSerializer
    http_method_names = ['get']

    def list(self, request):
        queryset = self.queryset.last()
        ser = self.serializer_class(queryset)
        return Response(ser.data)


class NumberFactView(ReadOnlyModelViewSet):
    queryset = NumberFact.objects.all()
    serializer_class = NumberFactSerializer
    http_method_names = ['get']

    def list(self, request):
        queryset = self.queryset.order_by('-id')[:3]
        ser = self.serializer_class(queryset, many=True)
        return Response(ser.data)


class InfoView(ReadOnlyModelViewSet):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer
    http_method_names = ['get']

    def list(self, request):
        queryset = self.queryset.last()
        ser = self.serializer_class(queryset)
        return Response(ser.data)


class LogoView(ReadOnlyModelViewSet):
    queryset = Info.objects.all()
    serializer_class = LogoSerializer
    http_method_names = ['get']

    def list(self, request):
        queryset = self.queryset.last()
        ser = self.serializer_class(queryset)
        return Response(ser.data)