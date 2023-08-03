from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SuperSerializer
from .models import Super

@api_view(['GET', 'POST'])
def super(request):
    
    if request.method == 'GET':

        super_type = request.query_params.get('super_type')
        print(super_type)

        queryset = Super.objects.all()

        if super_type:
            queryset = queryset.filter(super_type=super_type)

        serializer = SuperSerializer(queryset, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = SuperSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])        
def super_type(request, pk):
    car = get_object_or_404(Super, pk=pk)
    if request.method == 'GET':
        serializer = SuperSerializer(car);
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SuperSerializer(super, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        super.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET'])
def supers_by_id(request, id) :
    supers = Super.objects.all()
    supers_make = supers.filter(id=id)

    if supers_by_id:
        serializer = SuperSerializer(supers_by_id, many=True)
        return Response(serializer.data)
    else:
        return Response("No cars of that make in the database!", status=status.HTTP_404_NOT_FOUND)
      
