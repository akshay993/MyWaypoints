
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

urlpatterns = [
    #path('maps/', include('maps.urls')),

    path('admin/', admin.site.urls),
    url(r'^maps/', include('maps.urls')),

]
