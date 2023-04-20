from django.contrib import admin
from .models import Subject, Chapter, Topic, SubTopic


class SubTopicInline(admin.StackedInline):
    model = SubTopic
    extra = 1


class TopicInline(admin.StackedInline):
    model = Topic
    extra = 1
    inlines = [SubTopicInline]


class ChapterInline(admin.StackedInline):
    model = Chapter
    extra = 1
    inlines = [TopicInline]


class SubjectAdmin(admin.ModelAdmin):
    inlines = [ChapterInline]


admin.site.register(Subject, SubjectAdmin)
