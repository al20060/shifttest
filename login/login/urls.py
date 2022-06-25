from django.contrib import admin
from django.urls import path

from register.views import frontpage
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", frontpage),
]
