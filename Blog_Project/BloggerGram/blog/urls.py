from django.urls import path
from blog import views


# app_name = 'blog'

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('post/<pk:int>', views.PostDetailView.as_view(), name='post_detail'),
    path('post/new', view.CreatePostView.as_view(), name='post_new'),
    path('post/<pk:int>/edit', views.PostUpdateView.as_view(), name='post_edit'),
    path('post/<pk:int>/remove', views.PostDeleteView.as_view(), name='post_remove'),
    path('drafts/', views.DraftListView.as_view(), name='post_draft_list'),
    path('post/<pk:int>/comment', views.add_comment_to_post, name='add_comment_to_post')

]
