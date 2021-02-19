from django.urls import path

from .views import NoteList, NoteDetail, UserList, UserDetail

urlpatterns = [
    path('notes/<int:pk>/', NoteDetail.as_view()),
    path('notes/', NoteList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
    path('users/', UserList.as_view()),
]