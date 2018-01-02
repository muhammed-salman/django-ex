from django.conf.urls import url
from basicapp import views #can also use from . import views

#template tagging
app_name = 'basic_app'
urlpatterns=[
    url(r'^relative/$',views.relative,name='relative'),
    url(r'^other/$',views.other,name='other'),
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login')
]
