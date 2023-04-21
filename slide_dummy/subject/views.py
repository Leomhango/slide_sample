from rest_framework import generics
from .models import Subject, Chapter, Topic, SubTopic
from .serializers import SubjectSerializer, ChapterSerializer, TopicSerializer, SubTopicSerializer


class SubjectList(generics.ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class SubjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class ChapterList(generics.ListCreateAPIView):
    serializer_class = ChapterSerializer

    def get_queryset(self):
        subject_id = self.kwargs.get('subject_id')
        return Chapter.objects.filter(subject_id=subject_id)


class ChapterDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ChapterSerializer
    queryset = Chapter.objects.all()


class TopicList(generics.ListCreateAPIView):
    serializer_class = TopicSerializer

    def get_queryset(self):
        chapter_id = self.kwargs.get('chapter_id')
        return Topic.objects.filter(chapter_id=chapter_id)


class TopicDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TopicSerializer
    queryset = Topic.objects.all()


class SubTopicList(generics.ListCreateAPIView):
    serializer_class = SubTopicSerializer

    def get_queryset(self):
        topic_id = self.kwargs.get('topic_id')
        return SubTopic.objects.filter(topic_id=topic_id)


class SubTopicDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SubTopicSerializer
    queryset = SubTopic.objects.all()
