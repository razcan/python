from django.contrib import admin
from django.urls import include, path
from chart import views

urlpatterns = [
    path('', include('chart.urls')),
    #path('chart/', include('chart.urls')), --daca dorim sa avem ruta cu ip/chart
    path('admin/', admin.site.urls),
]