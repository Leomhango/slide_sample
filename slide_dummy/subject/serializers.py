from rest_framework import serializers
from .models import Subject, Chapter, Topic, SubTopic


class SubTopicSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SubTopic
        fields = ['id', 'url', 'title', 'content',]


class TopicSerializer(serializers.HyperlinkedModelSerializer):
    subtopics = SubTopicSerializer(many=True, read_only=True)

    class Meta:
        model = Topic
        fields = ['id', 'url', 'title', 'content', 'subtopics']


class ChapterSerializer(serializers.ModelSerializer):
    topics = TopicSerializer(many=True, read_only=True)

    class Meta:
        model = Chapter
        fields = ['id', 'url', 'title', 'description', 'topics']


class SubjectSerializer(serializers.ModelSerializer):
    chapters = ChapterSerializer(many=True, read_only=True)

    class Meta:
        model = Subject
        fields = ['id', 'url', 'name', 'chapters']
