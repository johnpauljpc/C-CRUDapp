from django.urls import path
from .views import (HomeView, Create_View,
	Detail_View, Update_View, Delete_View)


urlpatterns = [
	path('', HomeView.as_view(), name = 'home'),
	path('new/', Create_View.as_view(), name = 'create'),
	path('detail/<pk>/', Detail_View.as_view(), name = 'detail'),
	path('update/<pk>/', Update_View.as_view(), name = 'update'),
	path('delete/<pk>/', Delete_View.as_view(), name = 'delete'),
]