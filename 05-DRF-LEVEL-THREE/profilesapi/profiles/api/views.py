from rest_framework import generics
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework import mixins
from profiles.models import Profile, ProfileStatus
from profiles.api.serializers import ProfileAvatarSerializer, ProfileSerializer, ProfileStatusSerializer
from profiles.api.permissions import IsOwnProfileOrReadOnly, IsOwnOrReadOnly

class ProfileViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin):
    queryset = Profile.objects.all().order_by('-id')

    serializer_class = ProfileSerializer

    permission_classes = [IsAuthenticated ,IsOwnProfileOrReadOnly]



class ProfileStatusViewSet(ModelViewSet):
    queryset = ProfileStatus.objects.all().order_by('-id')

    serializer_class = ProfileStatusSerializer

    permission_classes = [IsAuthenticated ,IsOwnOrReadOnly]

    def perform_create(self, serializer):
        user_profile = self.request.user.profile
        serializer.save(user_profile=user_profile)
        return super().perform_create(serializer)


class AvatarUpdateView(generics.UpdateAPIView):
    serializer_class = ProfileAvatarSerializer
    
    permission_classes = [IsAuthenticated]

    def get_object(self):
        profile_object = self.request.user.profile
        return profile_object


# class ProfileViewSet(ReadOnlyModelViewSet):
#     queryset = Profile.objects.all().order_by('-id')

#     serializer_class = ProfileSerializer

#     permission_classes = [IsAuthenticated]


# class ProfileList(generics.ListAPIView):
#     queryset = Profile.objects.all().order_by('-id')

#     serializer_class = ProfileSerializer

#     permission_classes = [IsAuthenticated]