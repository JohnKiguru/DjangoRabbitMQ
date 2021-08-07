import requests
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework import mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import *
from .producer import publish
from .serializers import *

class QuoteViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = QuoteSerializer
    queryset = Quote.objects.all()

class QuoteUserViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = QuoteUserSerializer
    queryset = QuoteUser.objects.all()

@api_view(['GET'])
def like(request, pk, format=None):

    query = {'username': 'john'}
    req = requests.get('http://127.0.0.1:8000/users', params=query)
    data = req.json()
    print(data)


    try:
        for s in range(len(data)):
            if data[s]['id']:
                quoteuser = QuoteUser.objects.create(user_id=data[s]['id'], quote_id=pk)
                quoteuser.save()
                publish('quote_liked', pk)
                print('Quoteuser created')
                return Response('Quote liked...', status=status.HTTP_201_CREATED)
    except:

        return Response("Quote already liked...",status=status.HTTP_400_BAD_REQUEST)

