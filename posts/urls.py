from django.urls import path
from .views import (PostListView,
                    PostDetailView,
                    PostCreateView,
                    PostUpdateView,
                    PostDeleteView
                    )
from . import views


urlpatterns = [
    path('', PostListView.as_view(), name='posts-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='posts-detail'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='posts-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='posts-delete'),
    path('post/new/', PostCreateView.as_view(), name='posts-create'),
    path('about/', views.about, name='about'),
]
