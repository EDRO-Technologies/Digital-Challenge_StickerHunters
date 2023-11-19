from django.forms import model_to_dict
from rest_framework import permissions, viewsets
from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import GenericAPIView, CreateAPIView, RetrieveAPIView, ListCreateAPIView
from .serializers import GroupSerializer, UserSerializer, FormSerializer
from rest_framework.views import APIView
from rest_framework import generics
from .models import User, Form
from rest_framework.response import Response


def form(request):
    return render(request, "form.html")


def auth(request):
    return render(request, "auth.html")

# class UserView(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

class userAPIView(APIView):
    def post(self, request):
        usernew = User.objects.create(
            name=request.data["name"],
            password=request.data["password"],
        )
        return Response({'post': model_to_dict(usernew)})


class Stats(GenericAPIView):
    permissions_class = ()
    serializer_class = FormSerializer
    queryset = Form.objects.all()
    def get(self, request):
        index = FormSerializer(self.get_queryset(), many=True)
        context = {
            "object_list": index.data,
        }
        return render(request, "stat.html", context=context)
