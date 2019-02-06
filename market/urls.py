from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic.base import TemplateView
from users import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('users.urls')),
    path('home/', include('themes.urls')),
    path('details/', include('details.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# urlpatterns += [
    
#     # re_path('(.*)', TemplateView.as_view(template_name='base.html'), name="base"),
# ]