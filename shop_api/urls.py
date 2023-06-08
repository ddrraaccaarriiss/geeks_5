from django.conf.urls.static import static
from shop_api import settings
from django.contrib import admin
from django.urls import path, include
from product import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/categories/', views.CategoryAPIView.as_view({'get': 'list', 'post': 'create'})),
    path('api/v1/categories/<int:id>/', views.CategoryAPIView.as_view({'get': 'retrieve',
                                                                       'put': 'update',
                                                                       'delete': 'destroy'})),
    path('api/v1/products/', views.ProductsAPIView.as_view({'get': 'list', 'post': 'create'})),
    path('api/v1/products/<int:id>/', views.ProductsAPIView.as_view({'get': 'retrieve',
                                                                     'put': 'update',
                                                                     'delete': 'destroy'})),
    path('api/v1/reviews/', views.ReviewsAPIView.as_view({'get': 'list', 'post': 'create'})),
    path('api/v1/reviews/<int:id>/', views.ReviewsAPIView.as_view({'get': 'retrieve',
                                                                   'put': 'update',
                                                                   'delete': 'destroy'})),
    path('api/v1/products/reviews/', views.ProductsReviewsAPIView.as_view()),
    path('api/users/', include('users.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
