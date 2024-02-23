from rest_framework import generics, permissions
from .models import Content
from .serializers import ContentSerializer

class IsAuthorOrAdminOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Allow read-only permissions for any request.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Allow write permissions for admins or if the user is the author of the content.
        return request.user.is_staff or obj.author == request.user

class ContentListCreateView(generics.ListCreateAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class ContentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    permission_classes = [IsAuthorOrAdminOrReadOnly]