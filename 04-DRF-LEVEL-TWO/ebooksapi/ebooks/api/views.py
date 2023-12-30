from rest_framework import generics
from rest_framework import mixins
from rest_framework import permissions
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404

from ebooks.models import Ebook, Review
from ebooks.api.paginations import SmallSetPagination
from ebooks.api.serializers import EbookSerializer, ReviewSerializer
from ebooks.api.permissions import IsAdminUserOrReadOnly, IsReviewAuthorOrReadOnly

class EbookListCreateAPIView(generics.ListCreateAPIView):

    queryset = Ebook.objects.all().order_by('-id')
    permission_classes = [IsAdminUserOrReadOnly]
    serializer_class = EbookSerializer
    pagination_class = SmallSetPagination


class EbookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer
    permission_classes = [IsAdminUserOrReadOnly]

class ReviewCreateAPIView(generics.CreateAPIView):

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        ebook_pk = self.kwargs.get('ebook_pk')
        
        ebook = get_object_or_404(Ebook, pk=ebook_pk)
        
        review_author = self.request.user

        review_query = Review.objects.filter(ebook=ebook, review_author=review_author)

        if review_query.exists():
            raise ValidationError("You have Already Reviewed this Book")

        serializer.save(ebook=ebook, review_author=review_author)


class ReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsReviewAuthorOrReadOnly]


# class EbookListCreateAPIView(
#                         generics.GenericAPIView, 
#                         mixins.CreateModelMixin,
#                         mixins.ListModelMixin):
    
#     queryset = Ebook.objects.all()
#     serializer_class = EbookSerializer
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
    

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
