from rest_framework import serializers

from tours.models import CategoryModel, TourModel


class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = '_all_'


class ToursModelSerializer(serializers.ModelSerializer):
    category = CategoryModelSerializer()

    class Meta:
        model = TourModel
        fields = '_all_'
