from rest_framework import serializers

from .models import NewsInstance, NewsTag

class NewsTagSerializer(serializers.ModelSerializer):

    class Meta:
        model = NewsTag
        fields = ['id', 'news', 'tag']

class NewsSerializer(serializers.ModelSerializer):

    tags = NewsTagSerializer(many = True, read_only = True)

    validated_tags = serializers.ListField(
        child = serializers.CharField(),
        write_only = True,
        required = False
    )

    class Meta:
        model = NewsInstance
        fields = ['id', 'title', 'annotation', 'content', 'datetime', 'image_url', 'url', 'tags', 'validated_tags']

    def create(self, validated_data):

        validated_tags = validated_data.pop("validated_tags", [])

        news_object = NewsInstance.objects.create(**validated_data)

        for tag in validated_tags:

            NewsTag.objects.create(news = news_object, tag = tag)

        return news_object