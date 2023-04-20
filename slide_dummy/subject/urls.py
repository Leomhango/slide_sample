from django.urls import path
from .views import SubjectList

urlpatterns = [
    path('subject/', SubjectList.as_view(), name="subject")
]
