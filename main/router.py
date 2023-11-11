from rest_framework.routers import DefaultRouter
from .views import *


router = DefaultRouter()


router.register('main_banner', MainBannerView, basename='MainBanner')
router.register('order', OrderView, basename='Order')
router.register('discount', DiscountView, basename='Discount')
router.register('products', ProductView, basename='Product')
router.register('info_about_product', InfoAboutProductView, basename='InfoAboutProduct')
router.register('about_company', AboutCompanyView, basename='AboutCompany')
router.register('diseases', DiseaseBannerView, basename='DiseaseBanner')
router.register('how_to_use', HowToUseView, basename='HowToUse')
router.register('number_facts', NumberFactView, basename='NumberFact')
router.register('info', InfoView, basename='Info')
