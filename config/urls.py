from django.contrib import admin
from django.urls import path, include
from pybo.views import base_views
# from pybo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('pybo/', views.index),
    path('pybo/', include('pybo.urls')),
    path('common/', include('common.urls')),
    path('', base_views.index, name='index'), # '/'에 해당되는 path
]
