from django.shortcuts import render

from api.models import todos
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
import json
def read_todos():
    with open("D:\\Django_works\\todoapi\\api\\todos.json", "r") as f:
        data = json.load(f)
    return data

class Todos(APIView):
    def get(self,request,*args,**kwargs):
        data=read_todos()
        return Response({"data":data},status=status.HTTP_200_OK)

class TodoDetails(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        data=read_todos()
        try:
            todo=[todo for todo in data if todo["id"]==id][0]
            return Response({"todo":todo},status=status.HTTP_200_OK)
        except:
            return Response({"msg":"invalid id"},status=status.HTTP_400_BAD_REQUEST)

class MyTodos(APIView):
    def get(self,request,*args,**kwargs):
        userid=request.query_params.get("userid")
        completed=request.query_params.get("completed")
        data=read_todos()
        qs=[todo for todo in data if(todo["userId"]==int(userid))&(todo["completed"]==completed)]
        return Response({"data":qs},status=status.HTTP_200_OK)
