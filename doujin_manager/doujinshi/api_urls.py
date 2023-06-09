from django.urls import path, re_path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # list
    re_path(r"^circle/list/", view=views.CircleListView.as_view(), name="circle list"),
    re_path(r"^author/list/", view=views.AuthorListView.as_view(), name="author list"),
    re_path(r"^doujinshi/list/", view=views.DoujinshiListView.as_view(), name="doujinshi list"),
    # get/modify single data
    re_path(r"^circle/(?P<id>\d+)/", view=views.circle_id_view, name="circle get/modify by id"),
    re_path(r"^author/(?P<id>\d+)/", view=views.author_id_view, name="author get/modify by id"),
    re_path(r"^doujinshi/(?P<id>\d+)/", view=views.doujinshi_id_view, name="doujinshi get/modify by id"),
    # create data
    re_path(r"^circle/", view=views.circle_create_destory_view, name="circle create/delete"),
    re_path(r"^author/", view=views.author_create_destory_view, name="author create/delete"),
    re_path(r"^doujinshi/", view=views.doujinshi_create_destory_view, name="doujinshi create/delete"),
    # choices
    re_path(r"choices/", view=views.choice_view, name="all choices"),
]
