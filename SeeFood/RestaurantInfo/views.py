from django.shortcuts import render
from navigation.models import Restaurant, FoodItem
from django.views import generic
# Create your views here.

class RestaurantDetailView(generic.DetailView):
	model = Restaurant
	template_name = "RestaurantInfo/templates/restaurant_detail.html"


class FoodItemDetailView(generic.DetailView):
	model = FoodItem
	template_name = "RestaurantInfo/templates/fooditem_detail.html"