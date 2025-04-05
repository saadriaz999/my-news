from django.urls import path
from .views import ArticleListCreateView, ArticleRetrieveUpdateDestroyView, ArticleFetchView

urlpatterns = [
    path("", ArticleListCreateView.as_view(), name="article-list-create"),
    path("<int:pk>/", ArticleRetrieveUpdateDestroyView.as_view(), name="article-detail"),
    path("fetch/", ArticleFetchView.as_view(), name="fetch-articles")
]
