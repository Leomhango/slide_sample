from rest_framework import serializers
from .models import Subject, Chapter, Topic, SubTopic


class SubTopicSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SubTopic
        fields = '__all__'


class TopicSerializer(serializers.HyperlinkedModelSerializer):
    subtopics = SubTopicSerializer(many=True, read_only=True)

    class Meta:
        model = Topic
        fields = '__all__'


class ChapterSerializer(serializers.HyperlinkedModelSerializer):
    topics = TopicSerializer(many=True, read_only=True)

    class Meta:
        model = Chapter
        fields = '__all__'


class SubjectSerializer(serializers.HyperlinkedModelSerializer):
    chapters = ChapterSerializer(many=True, read_only=True)

    class Meta:
        model = Subject
        fields = ['url', 'name', 'chapters']
