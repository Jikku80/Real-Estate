from django.urls import path
from .views import RealtorListView, RealtorView, TopSellerView

urlpatterns = [
    path('', RealtorListView.as_view(), name='list'),
    path('topseller/', TopSellerView.as_view(), name='topseller'),
    path('<pk>/', RealtorView.as_view(), name='detail'),
]
