"""beer_rater URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from ratings.views import home, RatingCreate, RatingEdit

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name='rating-home'),
    url(r'rating/add/$', RatingCreate.as_view(), name='rating-add'),
    url(r'rating/edit/(?P<rating_id>\d+)/$', RatingEdit.as_view(), name='rating-edit'),
]
