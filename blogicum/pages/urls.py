from django.urls import path, include

from django.views.generic.base import TemplateView as tv

app_name = 'pages'

urlpatterns = [
    path('about/', tv.as_view(template_name="pages/about.html"), name='about'),
    path('rules/', tv.as_view(template_name="pages/rules.html"), name='rules'),
    path('blog/', include('blog.urls', namespace='blog')),
]
