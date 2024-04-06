from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Run
from .serializers import RunSerializer


class RunListCreateView(APIView):
    def get(self, request, format=None):
        runs = Run.objects.all()
        serializer = RunSerializer(runs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RunSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_BAD_REQUEST)


class RunDetailView(APIView):
    def get_object(self, pk):
        try:
            return Run.objects.get(pk=pk)
        except Run.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        run = self.get_object(pk)
        serializer = RunSerializer(run)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        run = self.get_object(pk)
        serializer = RunSerializer(run, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        run = self.get_object(pk)
        run.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
