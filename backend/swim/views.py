from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Swim
from .serializers import SwimSerializer


class SwimListCreateView(APIView):
    def get(self, request, format=None):
        swims = Swim.objects.all()
        serializer = SwimSerializer(swims, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = SwimSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SwimDetailView(APIView):
    def get_object(self, pk):
        try:
            return Swim.objects.get(pk=pk)
        except Swim.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        swim = self.get_object(pk)
        serializer = SwimSerializer(swim)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        swim = self.get_object(pk)
        serializer = SwimSerializer(swim, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        swim = self.get_object(pk)
        swim.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
