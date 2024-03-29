"""reader URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from files.views import FileViewSet
from books.views import BookViewSet
from pages.views import PageViewSet
from categories.views import BookCategoryViewSet

router = DefaultRouter()
router.register(r'api/files', FileViewSet, basename='file')
router.register(r'api/books', BookViewSet, basename='book')
router.register(r'api/pages', BookViewSet, basename='page')
router.register(r'api/book-categories', BookCategoryViewSet, basename='book-categories')


urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += router.urls
