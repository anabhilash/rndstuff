from django.conf.urls import url,patterns,include
from classview import *

urlpatterns = patterns('',
                        url(r'^todolist/$',TodoListView.as_view(),name="todolistview"),

                        url(r'^todolist/create',TodoListCreate.as_view(),name='todolistcreate'),

                        url(r'^todolist/update/(?P<pk>[0-9]+)/$',TodoListUpdate.as_view(),name='todolistupdate'),

                        url(r'^todolist/delete/(?P<pk>[0-9]+)/$',TodoListDelete.as_view(),name='todolistdelete'),

                        url(r'^todolist/(?P<id>[0-9]+)/items/$',TodoItemList.as_view(),name="todoitemlist"),

                        url(r'^todolist/(?P<id>[0-9]+)/items/create',TodoItemCreate.as_view(),name="todoitemcreate"),

                        url(r'^todolist/(?P<listid>[0-9]+)/items/(?P<pk>[0-9]+)/update',TodoItemUpdate.as_view(),name="todoitemupdate"),

                        url(r'^todolist/(?P<listid>[0-9]+)/items/(?P<pk>[0-9]+)/delete',TodoItemDelete.as_view(),name="todoitemdelete")
                     )