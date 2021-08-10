from django.urls import path
from .import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.postblog,name='Home'),
    path('Post/<int:id>/',views.detailblog, name='Details'),

]

urlpatterns += staticfiles_urlpatterns()