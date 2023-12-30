from django.urls import path, include

from rest_framework.routers import DefaultRouter

from profiles.api import views
router = DefaultRouter()

router.register("profiles", views.ProfileViewSet)
router.register("status", views.ProfileStatusViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("avatar/", views.AvatarUpdateView.as_view(), name='avatar')
]


# profile_list = views.ProfileViewSet.as_view({"get": "list"})
# profile_detail = views.ProfileViewSet.as_view({"get": "retrieve"})

# urlpatterns = [
#     #path("profile-list/", views.ProfileList.as_view(), name="profile-list"),
#     path("profiles/", profile_list, name="profile-list"),
#     path("profile/<pk>/", profile_detail, name="profile-detail"),
    
# ]
