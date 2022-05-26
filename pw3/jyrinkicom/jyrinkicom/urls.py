from django.contrib import admin
from django.urls import path
from exerciseapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('entries/', views.EntryListView.as_view()),
    path('entries/<int:pk>', views.EntryDetailView.as_view()),
    path('entries/<int:pk>/update', views.EntryUpdateView.as_view()),
    path('entries/<int:pk>/delete', views.EntryDeleteView.as_view()),
    path('entries/new', views.EntryCreateView.as_view()),
]
