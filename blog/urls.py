from django.urls import path
from . import views


app_name = 'blog'
urlpatterns = (
    path('articles/<int:page>/', views.Articles.as_view(), name='articles'),
    path('comment/', views.CreateCommentView.as_view(), name='create_comment'),
)
