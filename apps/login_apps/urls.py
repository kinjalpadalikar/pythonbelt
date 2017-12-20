from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^login$', views.login),
    url(r'^register$', views.register),
    url(r'^logout$', views.logout),
    url(r'^friends$', views.friends),
    url(r'^users/(?P<id>\d+)$', views.profile),
    url(r'^users/add/(?P<id>\d+)$', views.add_friend),
    url(r'^users/remove/(?P<id>\d+)$', views.remove_friend),
]
    


    
    
    
   




















# urlpatterns = [
#     url(r'^$', views.index),
#     url(r'^login$', views.login),
#     url(r'^users/new$', views.new),
#     url(r'^users/create$', views.create),
#     url(r'^users/(?P<user_id>\d+)$', views.show),
#     url(r'^users/(?P<user_id>\d+)/edit$', views.edit),
#     url(r'^users/(?P<user_id>\d+)/update$', views.update),
#     url(r'^users/(?P<user_id>\d+)/destroy$', views.destroy)

   
# ]



# from django.conf.urls import url
# from . import views

# urlpatterns = [
#     url(r'^$', views.index, name="index"),
#     url(r'^add$', views.add, name="add"),
#     url(r'^create', views.create, name="create"),
#     url(r'^(?P<book_id>\d+)$', views.show),
#     url(r'^(?P<book_id>\d+)/create$', views.create_additional)
# ]