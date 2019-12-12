from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from posts.views import index, blog, post, contact, about, InstaView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('insta/', InstaView.as_view(template_name='insta.html', extra_context={
        "instagram_profile_name": "amd"
    })),
    path('contact/', contact),
    path('about/', about),
    path('blog/', blog, name='post-list'),
    path('post/<slug>/', post, name='post-detail'),
    path('tinymce/', include('tinymce.urls')),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
