# -*- coding: utf-8 -*-
from django.urls import path

from comments.views import CommentCreateViews#, CommentView

urlpatterns = [
    # path('comments', CommentView.as_view(), name='comments'),
    path('createcomments', CommentCreateViews.as_view(), name='createcomments'),
]