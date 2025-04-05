from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Article
from .serializers import ArticleSerializer
from .utils import get_previous_day_articles_by_category

# List and Create Articles
class ArticleListCreateView(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

# Retrieve, Update, and Delete a Single Article
class ArticleRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleFetchView(APIView):
    """
    This view fetches articles from the previous day for a list of categories,
    saves them to the database, and returns a success message with the saved articles.
    """
    def post(self, request, *args, **kwargs):
        # Define the categories and API key
        categories = ['technology', 'health', 'business', 'sports']  # Example categories

        # Fetch and save the articles using your existing function
        get_previous_day_articles_by_category(categories)

        # Optionally serialize the saved articles
        serialized_articles = ArticleSerializer(Article.objects.all(), many=True)

        # Return a response with the success message and saved articles
        return Response({
            "message": "Articles for the previous day have been fetched and saved.",
            "articles": serialized_articles.data
        }, status=status.HTTP_200_OK)
