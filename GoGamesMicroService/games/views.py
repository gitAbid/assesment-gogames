from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from games.serializers import GameSerializer
from .models import Game


class GamesApi(APIView):

    def get(self, request):
        games = Game.objects.all()
        category = self.request.query_params.get('category_id', 0)
        if category is 0:
            serializer = GameSerializer(games, many=True)
        else:
            serializer = GameSerializer(games.filter(category=category), many=True)
        return Response(serializer.data)
