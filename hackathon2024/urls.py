from django.urls import path
from .views import AnalyzeView, MarketView, ChatView

urlpatterns = [
    path('analyze/', AnalyzeView.as_view(), name='analyze'),
    path('market/', MarketView.as_view(), name='market'),
    path('chat/', ChatView.as_view(), name='chat'),
]