from django.urls import path, include
import blog.views
app_name = 'blog'

urlpatterns = [
    path('', blog.views.PostListView.as_view(), name='post_list'),
    path('<int:pk>/', blog.views.PostDetailView.as_view(), name='post_detail'),
]
