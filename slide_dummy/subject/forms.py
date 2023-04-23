# forms.py
from django import forms
from .models import Subject, Chapter, Topic, SubTopic


class CreateChapter(forms.ModelForm):
    subject_name = forms.ModelChoiceField(
        queryset=Subject.objects.all(),
        required=True,
        empty_label=None,
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    chapter_title = forms.CharField(max_length=255)
    chapter_description = forms.CharField(widget=forms.Textarea)
    topic_title = forms.CharField(max_length=255)
    topic_content = forms.CharField(widget=forms.Textarea)
    subtopic_title = forms.CharField(max_length=255)
    subtopic_content = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = SubTopic
        fields = []

    def save(self, commit=True):
        # Check if a Subject object with the same name already exists
        subject, created = Subject.objects.get_or_create(
            name=self.cleaned_data['subject_name'])
        if created:
            # Create a new Chapter object if the Subject object is new
            chapter = Chapter.objects.create(
                title=self.cleaned_data['chapter_title'],
                description=self.cleaned_data['chapter_description'],
                subject=subject
            )
        else:
            # Get the existing Chapter object if the Subject object already exists
            chapter = Chapter.objects.get(
                title=self.cleaned_data['chapter_title'], subject=subject)
            if not chapter:
                # Create a new Chapter object if it doesn't exist
                chapter = Chapter.objects.create(
                    title=self.cleaned_data['chapter_title'],
                    description=self.cleaned_data['chapter_description'],
                    subject=subject
                )

        # Create a new Topic object
        topic = Topic.objects.create(
            title=self.cleaned_data['topic_title'],
            content=self.cleaned_data['topic_content'],
            chapter=chapter
        )

        # Create a new SubTopic object
        subtopic = SubTopic.objects.create(
            title=self.cleaned_data['subtopic_title'],
            content=self.cleaned_data['subtopic_content'],
            topic=topic
        )

        return subtopic
