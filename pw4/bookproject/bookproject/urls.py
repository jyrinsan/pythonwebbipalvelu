from django.contrib import admin
from django.urls import path
from bookapp import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', views.BookListView.as_view()),
    path('books/new', views.BookCreateView.as_view()),
    path('books/<int:pk>/', views.BookDetailView.as_view()),
    path('books/<int:pk>/update', views.BookUpdateView.as_view()),
    path('books/<int:pk>/delete', views.BookDeleteView.as_view()),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
	path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
]
