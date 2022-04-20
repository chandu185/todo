from django.shortcuts import render

from api.models import todos
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
import json


class Todos(APIView):
    def get(self,request,*args,**kwargs):
        with open("D:\\Django_works\\todoapi\\api\\todos.json","r") as f:
            data=json.load(f)
        return Response({"data":data},status=status.HTTP_200_OK)


