from django.urls import path
from . import views


urlpatterns=[
    path('',views.home,name="home"),
    path('post/<int:pk>/',views.post_detail,name="post_detail"),
    path('post/new/',views.post_new,name='post_new'),
    path('post/<int:pk>/edit/',views.post_edit,name='post_edit'),
    path('post/<int:pk>/remove/',views.post_remove,name='post_remove'),
    path('post/<int:pk>/comment/',views.add_comment,name='add_comment'),
]