from django.db import models


class Subject(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Chapter(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    subject = models.ForeignKey(
        Subject, on_delete=models.CASCADE, related_name='chapters')

    def __str__(self):
        return f"{self.subject.name}: {self.title}"


class Topic(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    chapter = models.ForeignKey(
        Chapter, on_delete=models.CASCADE, related_name='topics')

    def __str__(self):
        return f"{self.chapter.title}: {self.title}"


class SubTopic(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    topic = models.ForeignKey(
        Topic, on_delete=models.CASCADE, related_name='subtopics')

    def __str__(self):
        return f"{self.topic.title}: {self.title}"
