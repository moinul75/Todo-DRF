from django.shortcuts import render,HttpResponse
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated

from .models import Todo 
from .serializers import TodoSerializer


# Create your views here.
def home(request):
    return HttpResponse('Hi this is rest framework Home and server')


#for this we want to get the user login info
class Login(ObtainAuthToken):
    def post(self,request,*args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, create = Token.objects.get_or_create(user=user)
        return Response({'token':token.key, 'user_id':user.id})


class TodoListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated,]
    serializer_class = TodoSerializer
    
    #get this only for authentication user 
    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)
    
    
#now update the Todo and Delete the todo
class RetrieveTodoView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated,]
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    


    


    



