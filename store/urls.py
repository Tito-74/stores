from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)




urlpatterns = [
	path('store-list/', views.storeList, name="store-list"),
  path('store-detail/<str:pk>/', views.storeDetail, name="store-detail"),
  path('store-create/', views.StoreList.as_view(), name="store-create"),
  path('store-update/<str:pk>/', views.storeUpdate, name="store-update"),
  path('book-list/', views.BookListView.as_view(), name="book-list"),
  path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
  path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
  
	]