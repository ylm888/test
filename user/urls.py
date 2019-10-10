from django.conf.urls import url

from user import views

urlpatterns = [
    url(r'^sendsms/$',views.sendsms,name='sendsms'),
    url(r'^subcode/$',views.submit_code,name='subcode')
]