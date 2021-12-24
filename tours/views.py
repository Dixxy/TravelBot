from rest_framework.generics import ListAPIView

from tours.models import CategoryModel, TourModel
from tours.serializers import CategoryModelSerializer, ToursModelSerializer


class CategoryListAPIView(ListAPIView):
    serializer_class = CategoryModelSerializer
    queryset = CategoryModel.objects.all()


class TourListAPIView(ListAPIView):
    serializer_class = ToursModelSerializer

    def get_queryset(self):
        cat_pk = self.kwargs.get('cat_pk')
        q = self.request.GET.get('q')

        qs = TourModel.objects

        if cat_pk:
            return qs.filter(category_id=cat_pk)
        elif q:
            return qs.filter(title__icontains=q)
        else:
            return qs.none()
