"""insta_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter

from main.models import PostComment
from main.views import StoriesViewSet, PostViewSet, PostImageView, PostCommentView, LikeCreate
from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title='Jaseci API')

router = DefaultRouter()
router.register('posts', PostViewSet)
router.register('stories', StoriesViewSet)

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
schema_view = get_schema_view(
    openapi.Info(
        title="Jaseci API",
        default_version='v1',
        description="My instagram project",
        terms_of_service="https://www.jaseci.org",
        contact=openapi.Contact(email="jason@jaseci.org"),
        license=openapi.License(name="Awesome IP"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    re_path(r'^doc(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),
         name='schema-redoc'),
    path('docs/', schema_view),
    path('admin/', admin.site.urls),
    path('v1/api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('v1/api/add-image/', PostImageView.as_view()),
    path('v1/api/account/', include('user.urls')),
    path('v1/api/add-comment/', PostCommentView.as_view()),
    path('v1/api/<int:pk>/like/', LikeCreate.as_view()),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)









