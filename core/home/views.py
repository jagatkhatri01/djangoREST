from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Person, Address
from .serializers import PeopleSerializer, LoginSerializer

# Create your views here.
@api_view(['GET', 'POST', 'PUT'])
def index(request):
    courses = {
        'course_name':'python',
        'learn' : ['flask', 'django', 'fastApi'],
        'teacher': 'John',
    }
    if request.method == 'GET':
        print("YOU HIT A GET METHOD. ")
        return Response(courses)
    
    elif request.method == 'POST':
        print("YOU HIT A POST METHOD. ")
        return Response(courses)
    
    elif request.method == 'PUT':
        print("YOU HIT A PUT METHOD.")
        return Response(courses)
    
@api_view(['POST'])
def login(request):
    data = request.data
    serializer = LoginSerializer(data=data)
    if serializer.is_valid():
        data = serializer.data
        print(data)
        return Response({'message':'success'})
    return Response(serializer.errors)

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def person(request):
    if request.method == 'GET':
        objs = Person.objects.filter(address__isnull=False)
        serializer = PeopleSerializer(objs, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        data = request.data
        serializer = PeopleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    elif request.method == 'PUT':
        data = request.data
        serializer = PeopleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    elif request.method == 'PATCH':
        data = request.data
        objs = Person.objects.get(id = data['id'])
        serializer = PeopleSerializer(objs, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
     
     
    else:
        data = request.data
        objs = Person.objects.get(id=data['id'])
        objs.delete()