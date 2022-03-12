from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

import vendor
from .serializers import vendorSerializer

from .models import Vendor
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/vendor-list/',
		'Detail View':'/vendor-detail/<str:pk>/',
		'Create':'/vendor-create/',
		'Update':'/vendor-update/<str:pk>/',
		'Delete':'/vendor-delete/<str:pk>/',
		}

	return Response(api_urls)

@api_view(['GET'])
def taskList(request):
	tasks = vendor.objects.all().order_by('-id')
	serializer = vendorSerializer(tasks, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def taskDetail(request, pk):
	tasks = vendor.objects.get(id=pk)
	serializer = vendorSerializer(tasks, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def taskCreate(request):
	serializer = vendorSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def taskUpdate(request, pk):
	task = vendor.objects.get(id=pk)
	serializer = vendorSerializer(instance=task, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def taskDelete(request, pk):
	task = vendor.objects.get(id=pk)
	task.delete()

	return Response('Item succsesfully delete!')

