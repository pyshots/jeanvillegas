from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views
app_name = 'core'

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.CustomLoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(template_name="core/logout.html"), name="logout"),
    path('register/', views.register, name="register"),
    path('about/', views.about, name="about"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)