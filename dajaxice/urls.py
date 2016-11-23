old_style_url = False
try:
    from django.conf.urls import patterns, url
    old_style_url = True
except ImportError:
    try:
        from django.conf.urls.defaults import patterns, url
        old_style_url = True
    except ImportError:
        from django.conf.urls import url

from .views import DajaxiceRequest

if old_style_url:
    urlpatterns = patterns(
        'dajaxice.views',
        url(r'^(.+)/$', DajaxiceRequest.as_view(), name='dajaxice-call-endpoint'),
        url(r'', DajaxiceRequest.as_view(), name='dajaxice-endpoint'),
    )
else:
    urlpatterns = [
        # 'dajaxice.views',
        url(r'^(.+)/$', DajaxiceRequest.as_view(), name='dajaxice-call-endpoint'),
        url(r'', DajaxiceRequest.as_view(), name='dajaxice-endpoint'),
    ]

