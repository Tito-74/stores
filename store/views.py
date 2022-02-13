from django.shortcuts import render
from .serializers import StoreSerializer, BookSerializer
from .models import Store, Author 
from rest_framework import generics
from rest_framework import status
from functools import wraps

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
# Create your views here.
@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def storeList(request):
	store = Store.objects.all().order_by('-id')
	serializer = StoreSerializer(store, many=True)
	return Response(serializer.data)

@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def storeDetail(request, pk):
	store = Store.objects.get(id=pk)
	serializer = StoreSerializer(store, many=False)
	return Response(serializer.data)

# @api_view(['POST'])
# @permission_classes((IsAuthenticated, ))
# def storeCreate(request):
# 	serializer = StoreSerializer(data=request.data)

# 	if serializer.is_valid():
# 		serializer.save()

# 	return Response(serializer.data)
class StoreList(generics.ListCreateAPIView):
	querySet = Store.objects.all()
	permission_classes = [IsAuthenticated]
	serializer_class = StoreSerializer

	def create(self, request):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		self.perform_create(serializer)
		return Response({'message': f"store has been created"}, status=status.HTTP_201_CREATED)


@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
def storeUpdate(request, pk):
	store = Store.objects.get(id=pk)
	serializer = StoreSerializer(instance=store, data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)



class BookListView(generics.ListAPIView):
	permission_classes = (IsAuthenticated,)
	serializer_class = BookSerializer
	queryset = Store.objects.all()
	filter_fields = ('book_title','year_of_pub')