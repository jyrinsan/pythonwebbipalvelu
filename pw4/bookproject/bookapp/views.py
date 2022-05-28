from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from . import models
from django.contrib.auth.mixins import LoginRequiredMixin

class BookListView(ListView):
	model = models.Book

class BookDetailView(DetailView):
	model = models.Book

class BookUpdateView(LoginRequiredMixin, UpdateView):
	model = models.Book
	fields = ["title", "author"]
	success_url = "/books"

class BookCreateView(LoginRequiredMixin, CreateView):
	model = models.Book
	fields = ["title", "author"]
	success_url = "/books"

class BookDeleteView(LoginRequiredMixin, DeleteView):
	model = models.Book
	success_url = "/books"
