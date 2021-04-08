from django.urls import path,include

from .views import (Postindex,PostListView,PostDetailView,PostCreateView,PostDeleteView,PostUpdateView)

urlpatterns = [
    #path('',Postindex.as_view()),

    path('',PostListView.as_view(), name='PostListView'),
    path('<int:pk>/detail/',PostDetailView.as_view(),name='PostDetailView'),
    path('create/',PostCreateView.as_view(),name='PostCreateView'),
    path('<int:pk>delete/',PostDeleteView.as_view() , name='PostDeleteView'),
    path('<int:pk>/edit/',PostUpdateView.as_view(),name='PostUpdateView'),
]
