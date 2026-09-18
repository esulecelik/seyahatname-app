from django.urls import path
from . import views
urlpatterns = [
    path('location/',views.NoteListView.as_view(),name='notes'),
    path('location/<uuid:id>/',views.NoteView.as_view(),name='note-detail'),
]
