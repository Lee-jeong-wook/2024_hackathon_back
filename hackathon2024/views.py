from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import AnalyzeSerializer, MarketSerializer, ChatSerializer
from .services.analyze_service import AnalyzeService
from .services.market_service import MarketService
from .services.chat_service import ChatService

class AnalyzeView(APIView):
    analyze_service = AnalyzeService()

    def get(self, request):
        analyzes = self.analyze_service.get_all_analyzes()
        serializer = AnalyzeSerializer(analyzes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AnalyzeSerializer(data=request.data)
        if serializer.is_valid():
            analyze = self.analyze_service.create_analyze(serializer.validated_data)
            return Response(AnalyzeSerializer(analyze).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MarketView(APIView):
    market_service = MarketService()

    def get(self, request):
        markets = self.market_service.get_all_markets()
        serializer = MarketSerializer(markets, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MarketSerializer(data=request.data)
        if serializer.is_valid():
            market = self.market_service.create_market(serializer.validated_data)
            return Response(MarketSerializer(market).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ChatView(APIView):
    chat_service = ChatService()

    def get(self, request):
        chats = self.chat_service.get_all_chats()
        serializer = ChatSerializer(chats, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ChatSerializer(data=request.data)
        if serializer.is_valid():
            chat = self.chat_service.create_chat(serializer.validated_data)
            return Response(ChatSerializer(chat).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)