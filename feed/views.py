from django.shortcuts import render
from django.views.generic import TemplateView, FormView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .forms import PostForm
from django.http import HttpRequest, HttpResponse
from typing import Any
from .models import Post
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

class HomePage(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.order_by('-created_at').all()

        return context

# class AddPostFormPage(FormView):
#     template_name = 'add-post.html'
#     success_url = '/'
#     form_class = PostForm


#     def form_valid(self, form: Any) -> HttpResponse:
#         Post.objects.create(
#             title = form.cleaned_data['title'],
#             description = form.cleaned_data['description'],
#             image = form.cleaned_data['image']
#         )

#         messages.add_message(self.request,messages.SUCCESS, "Post has been added successfully")
     
#         return super().form_valid(form)

class AddPostFormPage(SuccessMessageMixin, CreateView):
    template_name = "post_create_form.html"
    model = Post
    fields = ["title", "description", "image"]
    success_url = '/'
    success_message = "%(title)s added successfully"

class PostDetailPage(DetailView):
    template_name = 'post_detail.html'
    model = Post

class PostDeletePage(SuccessMessageMixin, DeleteView):
    model = Post 
    template_name = 'post_detail.html'
    success_url = '/'
    
    def get_success_message(self, cleaned_data: dict[str, str]) -> str:
        return f'{self.object.title} has been deleted'

class PostUpdatePage(SuccessMessageMixin, UpdateView):
    model = Post 
    template_name = 'post_edit_form.html'
    success_url = '/'
    success_message = "%(title)s has been updated successfully"
    fields = ["title", "description", "image"]