from django.contrib import admin
from django.urls import include, path
from chart import views

urlpatterns = [
    path('chart/', include('chart.urls')),
    path('admin/', admin.site.urls),
]