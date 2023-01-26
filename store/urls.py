from rest_framework_extensions.routers import ExtendedDefaultRouter
from . import views
from django.urls import path
router = ExtendedDefaultRouter()


(
    router.register(r'categories',views.CategoryViewSet,basename='category')
          .register(r'subCategories',views.SubCategoryViewSet,basename='categories-subCategory',parents_query_lookups=['category__slug'])
          .register(r'products',views.ProductViewSet,basename='categories-subCategories-product',parents_query_lookups=('subCategory__category__slug','subCategory__slug'))
)

urlpatterns = [
    path('latest-products/',views.latestProducts,name='latest products'),
    path('navCategories/',views.navCategories),
    path('search/',views.search)
]+router.urls