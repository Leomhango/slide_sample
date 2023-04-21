from django.contrib import admin
from .models import Subject, Chapter, Topic, SubTopic


class SubTopicInline(admin.StackedInline):
    model = SubTopic
    extra = 1


class TopicAdmin(admin.ModelAdmin):
    inlines = [SubTopicInline]


admin.site.register(Topic, TopicAdmin)


class TopicInline(admin.StackedInline):
    model = Topic
    extra = 1
    show_change_link = True


class ChapterAdmin(admin.ModelAdmin):
    inlines = [TopicInline]


admin.site.register(Chapter, ChapterAdmin)


class ChapterInline(admin.StackedInline):
    model = Chapter
    extra = 1
    show_change_link = True


class SubjectAdmin(admin.ModelAdmin):
    inlines = [ChapterInline]


admin.site.register(Subject, SubjectAdmin)
