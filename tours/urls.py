from django.urls import path

from tours.views import CategoryListAPIView, TourListAPIView

app_name = 'tours'

urlpatterns = [
    path('categories/', CategoryListAPIView.as_view()),
    path('categories/<int:pk>/', TourListAPIView.as_view()),
    path('search/', TourListAPIView.as_view()),
]
