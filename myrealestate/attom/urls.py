from django.urls import path
from .views import PropertyList, PropertyDetail

urlpatterns = [
    path("propertylist/",  PropertyList.as_view(), name="propertylist"),
    path("propertydetail/<int:id>/",  PropertyDetail.as_view(), name="propertylist"),
]
