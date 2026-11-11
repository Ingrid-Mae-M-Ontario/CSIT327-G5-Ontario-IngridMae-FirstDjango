from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(pattern_name='profile', permanent=False)),
    path('', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]