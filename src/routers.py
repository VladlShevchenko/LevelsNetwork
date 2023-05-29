from django.urls import path, include

urlpatterns = [
    path('', include('src.profiles.urls')),
    path('wall/', include('src.wall.urls')),
    path('feed/', include('src.feed.urls')),
    path('follower/', include('src.followers.urls')),
]
