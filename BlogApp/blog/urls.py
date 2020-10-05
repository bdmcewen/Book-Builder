from django.urls import path
from django.views.generic import TemplateView


from .views import (
    BlogListView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
)

urlpatterns = [
    path('<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete'),
    path('new/', BlogCreateView.as_view(), name='post_new'),
    path('<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit'),
    path('', BlogListView.as_view(), name='post_list'),
    path('index', TemplateView.as_view(template_name="index.html"))
]
