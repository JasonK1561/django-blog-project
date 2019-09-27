from django.shortcuts import render, get_object_or_404, redirect,
from django.utils import timezone
from blog.models import Post, Comment
from django.contrib.auth.mixins import LoginRequiredMixin
from blog.forms import PostForm, CommentForm
from django.urls import reverse_lazy
from django.views.generic import (View, TemplateView,
                                ListView, CreateView,
                                UpdateView, DeleteView,
                                DetailView
)



# Create your views here.
class AboutView(TemplateView):
    template_name = 'about.html'


class PostListView(ListView):
    model = Post
    #post_list.html

    #This allows to use Djangos ORM
    #-pulished_date shows the most recent post
    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')


class PostDetailView(DetailView):
    model = Post


class CreatePostView(LoginRequiredMixin, CreateView):
    # Mix ins
    login_url = '/login/'
    #Login redirect to the view below
    redirect_field_name = 'blog/post_detail.html'

    form_class = PostForm

    model = Post


class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    #Login redirect to the view below
    redirect_field_name = 'blog/post_detail.html'

    form_class = PostForm

    model = Post


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    #Redirects your to a view after delete
    success_url = reverse_lazy('post_list')

class DraftListView(LoginRequiredMixin, ListView):
    model = Post
    login_url = '/login/'
    redirect_field_name = 'blog/post_list.html'

    #Return posts that do not have a published date, meaning they are drafts
    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('created_date')


####################################################
####################################################

#decorator
@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(post,pk=pk)
    if request.method == 'POST':
        form = CmmentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
        else:
            form = CommentForm()
        return render(request, 'blog/comment_form.html', {'form':form})

@login_required
def comment_approve(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    comment.approve()
    return redirect('post_detail',pk=comment.post.pk)
