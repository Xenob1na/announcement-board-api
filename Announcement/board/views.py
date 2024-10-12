from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, authentication, permissions

from .models import Announcement
from .serializers import BoardSerializer, BoardDetailSerializer
from .paginations import BoardPagination

class ListBoardView(APIView):
    def get(self, request):
        try:
            boards = Announcement.objects.all()
            serializer = BoardSerializer(boards, many=True)
            pagination = BoardPagination()
            page = pagination.paginate_queryset(serializer.data, request)
            return pagination.get_paginated_response(page)
        except Announcement.DoesNotExist:
            return Response({"message": "Таких объявлений не существует"},status=status.HTTP_404_NOT_FOUND)
        
class BoardDetailView(APIView):
    def get(self, request, pk):
        try:
            boards = Announcement.objects.get(pk=pk)
            serializer = BoardDetailSerializer(boards)
            return Response(serializer.data)
        except Announcement.DoesNotExist:
            return Response({"message": "Такого объявления не существует"}, status=status.HTTP_404_NOT_FOUND)