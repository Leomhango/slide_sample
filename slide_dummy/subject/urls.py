from django.urls import path
from .views import (
    SubjectList, SubjectDetail,
    ChapterList, ChapterDetail,
    TopicList, TopicDetail,
    SubTopicList, SubTopicDetail,
)

urlpatterns = [
    path('subjects/', SubjectList.as_view(), name='subject-list'),
    path('subjects/<int:pk>/', SubjectDetail.as_view(), name='subject-detail'),
    path('subjects/<int:subject_id>/chapters/',
         ChapterList.as_view(), name='chapter-list'),
    path('chapters/<int:pk>/', ChapterDetail.as_view(), name='chapter-detail'),
    path('chapters/<int:chapter_id>/topics/',
         TopicList.as_view(), name='topic-list'),
    path('topics/<int:pk>/', TopicDetail.as_view(), name='topic-detail'),
    path('topics/<int:topic_id>/subtopics/',
         SubTopicList.as_view(), name='subtopic-list'),
    path('subtopics/<int:pk>/', SubTopicDetail.as_view(), name='subtopic-detail'),
]
