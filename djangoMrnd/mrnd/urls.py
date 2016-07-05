from django.conf.urls import url,patterns
from views import *
from classviews import *
urlpatterns = patterns('',
                            url(r'^college/$',Collegelist.as_view(),name="testListview"),
                            url(r'^college/(?P<location>[A-Za-z]*)/$',Collegelist.as_view(),name='college'),
                            url(r'^college/(?P<pk>[0-9]*)$',TestDetailView.as_view(),name='collegedetail'),
                            url(r'^college/(?P<acronym>[a-zA-Z]*)/detail$',TestDetailView.as_view(),name='colegedetails'),
                            url(r'^college/create$',TestCreateViewCollege.as_view(),name="collegecreate"),
                            url(r'^student/create$',TestCreateViewStudent.as_view(),name='studentcreate'),
                            url(r'^college/update/(?P<id>[0-9]+)/$',TestUpdateViewCollege.as_view(),name='colegeupdate'),
                            url(r'^college/delete/(?P<pk>[0-9]+)',TestDeleteViewCollege.as_view(),name='collegedelete')
                      )