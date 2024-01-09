from django.urls import path, include

from django.views.generic.base import TemplateView as TV

app_name = 'pages'

urlpatterns = [
    path('about/', TV.as_view(template_name="pages/about.html"), name='about'),
    path('rules/', TV.as_view(template_name="pages/rules.html"), name='rules'),
    path('blog/', include('blog.urls', namespace='blog')),
]
