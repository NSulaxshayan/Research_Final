from django.contrib import admin
from django.urls import include, path




urlpatterns = [

    path("admin/", admin.site.urls),
    path("", include("authentication.urls")), # Auth routes - login / register
    path("", include("home.urls")), 
    path("", include("networkcapture.urls")),
    # path("", include("polls.urls")),
    
    
]
