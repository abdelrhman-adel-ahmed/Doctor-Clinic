import debug_toolbar
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls", namespace="core")),
    path("api/", include("api.urls", namespace="api")),
]

urlpatterns += [
    path("__debug__/", include(debug_toolbar.urls)),
]