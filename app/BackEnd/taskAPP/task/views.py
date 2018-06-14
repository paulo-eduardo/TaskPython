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
        serializer.create = datetime.now
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #Endpoint para listar todas as tarefas
    def get(self, request, format=None):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)


class Task(APIView):
    """
    Endpoints com pk
    """

    #Metodo para pegar tarefa especifica
    def get_object(self, pk):
        try:
            return Task.objects.get(pk=pk)
        except CallRecord.DoesNotExist:
            raise Http404

    #Endpoint para alterar tarefa
    def put(self, request, pk, format=None):
        task = self.get_object(pk)
        task.edited = datetime.now
        serializer = TaskSerializer(task)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        task = self.get_object(pk)
        task.removed = datetime.now
        serializer = TaskSerializer(task)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskStatus(APIView):
    """
    Apenas altera status da tarefa com pk enviada na url
    """

    #Endpoint para alterar status da task
    def put(self, request, pk, format=None):
        task = Task.get_object(pk)
        task.status = not task.status
        
        if task.status:
            task.concluded = datetime.now
        else:
            task.concluded = None

        serializer = TaskSerializer(task)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    