from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
        (r'^addId/([^/]+)/([^/]+)/', 'TichuDB.views.addId'),
        (r'^login/([^/]+)/([^/]+)/', 'TichuDB.views.login'),
        (r'^join/([^/]+)/', 'TichuDB.views.join'),
        (r'^startGame/([^/]+)/', 'TichuDB.views.startGame'),
        (r'^readyGame/([^/]+)/', 'TichuDB.views.readyGame'),
        (r'^startGame/([^/]+)/', 'TichuDB.views.startGame'),
        (r'^readyTurn/([^/]+)/([^/]+)/([^/]+)/', 'TichuDB.views.readyTurn'),
        (r'^throw/([^/]+)/([^/]+)/([^/]+)/([^/]+)/([^/]+)/', 'TichuDB.views.throw'),
        (r'^deal8/([^/]+)/([^/]+)/', 'TichuDB.views.deal8'),
        (r'^deal6/([^/]+)/([^/]+)/', 'TichuDB.views.deal6'),
        (r'^Tichu/([^/]+)/([^/]+)/([^/]+)/', 'TichuDB.views.LTchu'),
        (r'^sTichu/([^/]+)/([^/]+)/([^/]+)/', 'TichuDB.views.sTchu'),
        (r'^exCard/([^/]+)/([^/]+)/([^/]+)/', 'TichuDB.views.exCard'),
    # Examples:
    # url(r'^$', 'Tichu.views.home', name='home'),
    # url(r'^Tichu/', include('Tichu.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
