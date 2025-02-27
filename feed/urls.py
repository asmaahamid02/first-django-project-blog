from django.urls import path
from .views import HomePage, AddPostFormPage, PostDetailPage, PostDeletePage, PostUpdatePage

app_name = 'feed'

urlpatterns = [
    path('', HomePage.as_view(), name="index"),
    path('post/add/', AddPostFormPage.as_view(), name="add-post"),
    path('post/<int:pk>/', PostDetailPage.as_view(), name="post-detail"),
    path('post/<int:pk>/delete', PostDeletePage.as_view(), name="post-delete"),
    path('post/<int:pk>/update', PostUpdatePage.as_view(), name="post-update")
]