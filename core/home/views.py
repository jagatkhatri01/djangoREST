from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

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