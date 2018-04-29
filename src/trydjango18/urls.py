from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import TemplateView
from dashboard.views import DashBoardTemplateView,Myview

urlpatterns = [
    # Examples:
    url(r'^$', 'newsletter.views.home', name='home'),
    url(r'^contact/$', 'newsletter.views.contact', name='contact'),

    # By using TemplateView there is no need to set a fbv in view.py
    url(r'^about/$',DashBoardTemplateView.as_view(), name='about'),
    url(r'^myview/$',Myview.as_view(template_name='template.html'), name='myview'),
    url(r'^team/$', TemplateView.as_view(template_name='team.html'), name='team'),




    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)