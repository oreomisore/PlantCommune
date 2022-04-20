from django.urls import path
from .views import (PostListView, PostDetailView)


app_name = "blog"
urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('product/<pk>', PostDetailView.as_view(), name="post-detail"),

]


