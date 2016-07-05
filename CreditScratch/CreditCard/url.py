from django.conf.urls import url , patterns,include
from classviews import *
from viewsapi import *
from rest_framework import routers
router=routers.DefaultRouter()
router.register(r'^', CardDetailsviewset)
urlpatterns = patterns('',
                       url(r'^CardDetails/$',CardList.as_view(),name='CardDetails'),
                     url(r'^updateDetails/(?P<pk>[0-9]+)/$',CardUpdate.as_view(),name='UpdateDetals'),
                     url(r'^deleteDetails/(?P<pk>[0-9]+)/$', CardDelete.as_view(), name='deleteDetals'),
                     url(r'^createDetails/$', Cardcreate.as_view(), name='createDetals'),
                      )