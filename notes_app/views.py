from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Note

class NoteListView(ListView):
    model = Note
    template_name = 'home.html'

class NoteDetailView(DetailView):
    model = Note
    template_name = 'note_detail.html'

class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    template_name = 'note_new.html'
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class NoteEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Note
    template_name = 'note_edit.html'
    fields = ['title', 'body']

    def test_func(self):
        note = self.get_object()
        return self.request.user == note.author

class NoteDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Note
    template_name = 'note_delete.html'
    success_url = reverse_lazy('instaface:home')

    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.author
