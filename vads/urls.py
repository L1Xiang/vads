from django.conf.urls import patterns, url, include

from vads import views

screen_patterns = patterns(
                           '',
                           url(r'^$', views.ScreenListView.as_view(), name = 'lists'),
                           url(r'^d/(?P<slug>[-\w]+)/$', views.ScreenDetailView.as_view(), name = 'detail'),
                           url(r'^create/$', views.ScreenCreateView.as_view(), name = 'create'),
                           url(r'^e/(?P<slug>[-\w]+)/$', views.ScreenUpdateView.as_view(), name = 'update'),
                           url(r'^delete/(?P<slug>[-\w]+)/$', views.ScreenDeleteView.as_view(), name = 'delete'),
                           url(r'^accounts/', include('allauth.urls')),
                           )
ad_patterns = patterns(
                       '',
                       url(r'detail/(?P<slug>[-\w]+)/$', views.AdDetailView.as_view(), name='detail'),
                       url(r'create/$', views.AdCreateView.as_view(), name='create'),
                       )

ad_list_patterns = patterns(
                            '',
                            url(r'^$', views.AdListListView.as_view(), name='lists'),
                            url(r'create/$', views.AdListCreateView.as_view(), name = 'create'),
                            url(r'detail/(?P<slug>[-\w]+)/$', views.AdListDetailView.as_view(), name='detail'),
                            url(r'update/(?P<slug>[-\w]+)/$', views.AdListUpdateView.as_view(), name='update'),
                            )


profile_patterns = patterns(
                           '',
                           url(r'^detail/(?P<pk>[0-9]+)/$', views.UserProfieDetailView.as_view(), name='detail'),
                           #url(r'^create/$', views.UserProfileCreateView.as_view(), name='create'),
                           url(r'^update/(?P<pk>[0-9]+)/$', views.UserProfileUpdateView.as_view(), name='update'),
                           )

urlpatterns = patterns(
        '',
        url(r'^$', views.index, name='index'),
        url(r'^profile/', include(profile_patterns, namespace = 'profile')),
        url(r'^screen/', include(screen_patterns, namespace ='screen')),
        url(r'^ad/', include(ad_patterns, namespace='ad')),
        url(r'^ad_lists/', include(ad_list_patterns, namespace='ad_lists')),
        )
