"""turing_food URL Configuration"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('restaurants.urls', 'restaurants'), namespace='restaurants')),
    path('users/', include(('users.urls', 'users'), namespace='users')),
    path('addresses/', include(('addresses.urls', 'addresses'), namespace='addresses')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'core.views.handler404'
handler505 = 'core.views.505'
