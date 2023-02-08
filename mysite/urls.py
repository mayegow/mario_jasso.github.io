
from django.contrib import admin
from django.urls import path, include
from portfolio import urls
urlpatterns = [
    path('', include(urls)),
    path('admin/', admin.site.urls),

]
