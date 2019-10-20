from django.shortcuts import render
from classes.models import Classroom
from .serializers import ListSerializer, DetailSerializer, UpdateSerializer, CreateSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView, CreateAPIView


class ClassroomList(ListAPIView):
	queryset = Classroom.objects.all()
	serializer_class = ListSerializer


class ClassroomDetail(RetrieveAPIView):
	queryset = Classroom.objects.all()
	serializer_class = DetailSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'classroom_id'


class ClassroomUpdate(RetrieveUpdateAPIView):
	queryset = Classroom.objects.all()
	serializer_class = UpdateSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'classroom_id'

class ClassroomDelete(DestroyAPIView):
	queryset = Classroom.objects.all()
	lookup_field = 'id'
	lookup_url_kwarg = 'classroom_id'

class ClassroomCreate(CreateAPIView):
	serializer_class = CreateSerializer
	
	def perform_create(self, serializer):
		serializer.save(teacher=self.request.user)