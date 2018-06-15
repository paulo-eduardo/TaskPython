from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from task.serializers import TaskSerializer
from task.models import Task
from datetime import datetime

# Create your views here.
class TaskList(APIView):
    """
    Endpoints sem pk
    """

    #Endpoint para criar uma nova tarefa
    def post(self, request, format=None):
        serializer = TaskSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #Endpoint para listar todas as tarefas
    def get(self, request, format=None):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)


class TaskDetail(APIView):
    """
    Endpoints com pk
    """

    #Metodo para pegar tarefa especifica
    def get_object(self, pk):
        try:
            return Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            raise Http404

    #Endpoint para alterar tarefa
    def put(self, request, pk, format=None):
        task = self.get_object(pk)
        task.edited = datetime.now()
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, pk, format=None):
        task = self.get_object(pk)
        date = datetime.now()
        if(task.status):
            date = None
        data = {
            "status": not task.status,
            "concluded": date
        }
        
        serializer = TaskSerializer(task, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self, request, pk, format=None):
        task = self.get_object(pk)
        task.delete()
        return Response(status=status.HTTP_200_OK)