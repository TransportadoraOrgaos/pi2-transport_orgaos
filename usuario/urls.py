from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^cadastro$', views.cadastro, name='cadastro'),
    url(r'^login$', views.do_login, name='login'),
    url(r'^session_expired$', views.do_login_session_expired, name='session_expired'),
    url(r'^logout$', views.do_logout, name='logout'),
    url(r'^list$', views.list, name='list'),
    url(r'^denied$', views.denied, name='denied'),
    url(r'^user_delete/(?P<users_username>.*)$', views.del_User, name='user_delete')
]