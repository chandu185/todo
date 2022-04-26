from django.shortcuts import render
from todoapp.serializer import TodoSerializer
from todoapp.models import Todos
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.

class TodoCreateView(APIView):

    def get(self,request,*args,**kwargs):
        todos=Todos.objects.all()
        serializer=TodoSerializer(todos,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request,*args,**kwargs):
        serializer=TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)


class TodoDetail(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        todos=Todos.objects.get(id=id)
        serializer=TodoSerializer(todos)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def put(self,request,*args,**kwargs):
        id=kwargs.get("id")
        todos=Todos.objects.get(id=id)
        serializer=TodoSerializer(data=request.data,instance=todos)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,*args,**kwargs):
        id=kwargs.get("id")
        todos=Todos.objects.get(id=id)
        todos.delete()
        return Response({"msge":"deleted"},status=status.HTTP_200_OK)


from rest_framework import generics
from rest_framework import mixins

class TodoMixinList(generics.GenericAPIView,
                    mixins.ListModelMixin,
                    mixins.CreateModelMixin):

    serializer_class = TodoSerializer
    queryset = Todos.objects.all()
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class TodoMixinDetails(generics.GenericAPIView,
                       mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin):

    serializer_class = TodoSerializer
    queryset = Todos.objects.all()
    lookup_field = "id"

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)