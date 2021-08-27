from app import views
from django.conf.urls import url
#for template tagggin
app_name = 'app'   #this will help to call different pagres
urlpatterns = [
    url('relative',views.relative,name='relative'),
    url('other',views.other,name='other'),

]
