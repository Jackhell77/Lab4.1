from django.conf.urls import patterns, include, url
from bookmanage.views import insertBook,book,insertAuthor,delete,update,search
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'adoaccess.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$',search),
    url(r'^search/',search),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^insertBook/$', insertBook),
    url(r'book/',book),
    url(r'insertAuthor/',insertAuthor),
    url(r'^delete/',delete),
    url(r'^update/',update),
)