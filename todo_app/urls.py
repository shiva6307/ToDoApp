from django.contrib import admin
from django.urls import path, include
from tasks.views import signup_view  # our custom signup view

urlpatterns = [
    path("admin/", admin.site.urls),

    # Django’s built-in auth views: /accounts/login/, /accounts/logout/, etc.
    path("accounts/", include("django.contrib.auth.urls")),

    # Our custom signup page
    path("accounts/signup/", signup_view, name="signup"),

    # App routes (tasks)
    path("", include("tasks.urls")),
]
