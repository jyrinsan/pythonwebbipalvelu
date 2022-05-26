from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from . import models

class EntryListView(ListView):
	model = models.Entry

class EntryDetailView(DetailView):
	model = models.Entry

class EntryUpdateView(UpdateView):
	model = models.Entry
	fields = "__all__"
	success_url = "/entries"

class EntryCreateView(CreateView):
	model = models.Entry
	fields = "__all__"
	success_url = "/entries"

class EntryDeleteView(DeleteView):
	model = models.Entry
	success_url = "/entries"
