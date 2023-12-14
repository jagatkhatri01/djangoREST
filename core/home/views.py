from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Person, Address
from .serializers import PeopleSerializer, LoginSerializer
from rest_framework.views import APIView
from rest_framework import status, viewsets
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

class ListUser(APIView):
    def get(self, request):
        objs = Person.objects.filter(address__isnull=False)
        serializer = PeopleSerializer(objs, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        data = request.data
        serializer = PeopleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def put(self, request):
        data = request.data
        serializer = PeopleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def patch(self, request):
        data = request.data
        objs = Person.objects.get(id = data['id'])
        serializer = PeopleSerializer(objs, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
   
    def delete(self, request):
        data = request.data
        person_id = data.get('id')

        if person_id is not None:
            objs = Person.objects.filter(id=person_id)

            if objs.exists():
                objs.delete()
                return Response({"message": "Person deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
            else:
                return Response({"message": f"Person with id {person_id} not found."}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"message": "Please provide an 'id' in the request data."}, status=status.HTTP_400_BAD_REQUEST)

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


class PeopleViewSet(viewsets.ModelViewSet):
    serializer_class = PeopleSerializer
    queryset = Person.objects.all()
    def get_queryset(self):
        search = self.request.GET.get('search')
        queryset = Person.objects.all()

        if search:
            queryset = queryset.filter(first_name__startswith=search)

        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = PeopleSerializer(queryset, many=True)
        return Response({'status': 200, 'data': serializer.data})