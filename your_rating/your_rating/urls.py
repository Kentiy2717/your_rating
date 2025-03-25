from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls', namespace='pages')),
    path('casks/', include('casks.urls', namespace='casks')),
    path('users/', include('users.urls', namespace='users')),
    path('recipes/', include('recipes.urls', namespace='recipes')),
    path('drinks/', include('drinks.urls', namespace='drinks')),
    path('rating/', include('rating.urls', namespace='rating')),
]

handler404 = 'pages.views.page_not_found'
handler500 = 'pages.views.server_error'

# if settings.DEBUG:
#     import debug_toolbar
#     urlpatterns += (path('__debug__/', include(debug_toolbar.urls)),)

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )
