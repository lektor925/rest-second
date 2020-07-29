from rest_framework.routers import DefaultRouter

from product.views import ProductSetsViewset, RecipientViewset, OrderViewset

router = DefaultRouter()
router.register('products', ProductSetsViewset, basename='products')
router.register('recipients', RecipientViewset, basename='recipients')
router.register('orders', OrderViewset, basename='orders')
urlpatterns = router.urls
