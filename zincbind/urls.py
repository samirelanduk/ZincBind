"""URL redirects for ZincBind."""

from django.conf.urls import url
import zincbind.views as views

urlpatterns = [
 url(r"^data/$", views.data),
 url(r"^search/$", views.search),
 url(r"^$", views.home)
]
