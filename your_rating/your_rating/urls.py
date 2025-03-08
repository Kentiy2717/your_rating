from django.contrib import admin
from django.urls import include, path
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls', namespace='pages')),
    path('casks/', include('casks.urls', namespace='casks')),
    path('users/', include('users.urls', namespace='users')),
    path('recipes/', include('recipes.urls', namespace='recipes')),
]

handler404 = 'pages.views.page_not_found'
handler500 = 'pages.views.server_error'

# if settings.DEBUG:
#     import debug_toolbar
#     urlpatterns += (path('__debug__/', include(debug_toolbar.urls)),)
