from project.serializers import ProjectSerializer
from rest_framework.generics import RetrieveAPIView, ListAPIView
from .models import Project
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response


class TaskView(RetrieveAPIView):

    permission_classes = (IsAuthenticated,)
    serializer_class = ProjectSerializer

    def get_object(self):
        return Project.objects.get(pk=self.kwargs.get('pk'))


class ProjectView(ListAPIView):

    permission_classes = (IsAuthenticated,)
    serializer_class = ProjectSerializer

    # def get(self, request, *args, **kwargs):
    #     data = [project.project_name for project in Project.objects.all()]
    #     return Response(data, status=status.HTTP_200_OK)
    def get_queryset(self):
        return Project.objects.all()



