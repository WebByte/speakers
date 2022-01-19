from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/auth/', include('authapp.urls')),
    path('api/workrooms/', include('workroomsapp.urls')),
]
