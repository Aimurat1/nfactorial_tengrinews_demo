from django.shortcuts import render

from rest_framework import viewsets, status

from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import filters

from django_filters import rest_framework as third_filters

# Models

from api.models import NewsInstance, NewsTag
from api.serializers import NewsSerializer, NewsTagSerializer
from .paginations import CustomPagination

# Create your views here.
class NewsInstanceFilter(third_filters.FilterSet):
    tags = third_filters.CharFilter(method='filter_by_tags')

    class Meta:
        model = NewsInstance
        fields = ['datetime']

    def filter_by_tags(self, queryset, name, value):
        # Filter the queryset by tags
        return queryset.filter(tags__tag=value)
    
class NewsModelView(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = NewsInstance.objects.order_by('-datetime')
    serializer_class = NewsSerializer
    pagination_class = CustomPagination

    search_fields = ['title', 'annotation', 'tags__tag']
    filter_backends = (filters.SearchFilter, filters.OrderingFilter, )
    ordering_fields = ['datetime']

    def get_queryset(self):
        queryset = super().get_queryset()

        # Filter by tags (handle multiple tags)
        tags = self.request.query_params.getlist('tags')
        if tags:
            queryset = queryset.filter(tags__tag__in=tags).distinct()

        return queryset

    @action(detail=False, methods=['post'])
    def check_url(self, request, *args, **kwargs):
        
        data = request.data

        url = data['url']

        if NewsInstance.objects.filter(url = url).exists():
            return Response(
                data = {
                    "status": "News already exists"
                },
                status=status.HTTP_403_FORBIDDEN
            )

        else:
            return Response(
                data = {
                    "status": "News ok"
                },
                status=status.HTTP_200_OK
            )


