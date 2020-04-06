from django.urls import path
from . import views

urlpatterns = [
	path("/restaurants/<int:pk>",views.RestaurantDetailView.as_view(), name = "res-detail"),
	path("/restaurants/menu/<int:pk>",views.FoodItemDetailView.as_view(), name = "food-detail"),
]
