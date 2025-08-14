"""
URL configuration for wine_wiki project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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

from django.urls import path, include
from . import views
from django.views.generic.base import RedirectView
from django.views import generic
from django.contrib import admin

app_name = "wine_wiki"

urlpatterns = [
    path(
        "",
        RedirectView.as_view(url="home"),
    ),
    path(
        "home/",
        view=generic.TemplateView.as_view(template_name="wine_wiki/home.html"),
        name="home",
    ),
    path(
        "changelog",
        view=generic.TemplateView.as_view(template_name="wine_wiki/changelog.html"),
        name="changelog",
    ),
    path("wine-list/", view=views.WineListView.as_view(), name="wine-list"),
    path("wine/<int:pk>/", view=views.WineView.as_view(), name="wine"),
    path("update/<int:pk>/", view=views.WineUpdateView.as_view(), name="wine-update"),
    path(
        "update-producer/<int:pk>/",
        view=views.ProducerUpdateView.as_view(),
        name="prod-update",
    ),
    path("admin/", admin.site.urls),
    path("wine-create/", view=views.WineCreateView.as_view(), name="wine-create"),
    path("prod-create/", view=views.ProducerCreateView.as_view(), name="prod-create"),
    path(
        "wine-delete/<int:pk>/",
        view=views.WineDeleteView.as_view(),
        name="wine-delete",
    ),
    path(
        "prod-delete/<int:pk>/",
        view=views.ProducerDeleteView.as_view(),
        name="prod-delete",
    ),
    path("producer-list/", view=views.ProducerListView.as_view(), name="producer-list"),
    path("producer/<int:pk>/", view=views.ProducerView.as_view(), name="producer"),
    # path("accounts/", include("django.contrib.auth.urls")),  # new
    # path("sign_up/", view=views.SignUpView.as_view(), name="sign-up"),
]
