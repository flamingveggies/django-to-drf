from django.urls import path

from . import views

app_name = 'notes'

urlpatterns = [
    path('', views.NoteListView.as_view(), name='home'),
    path('note/<int:pk>/', views.NoteDetailView.as_view(), name='detail'),
    path('note/new/', views.NoteCreateView.as_view(), name='new'),
    path('note/<int:pk>/edit/', views.NoteEditView.as_view(), name='edit'),
    path('note/<int:pk>/delete/', views.NoteDeleteView.as_view(), name='delete'),
]