from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from rest_framework import generics
from .serializers import *
from .permissions import *
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrReadOnly
from django.contrib.auth import login, logout


class CategoryCreateView(generics.CreateAPIView):
    serializer_class = CategorySerializer


class CategoryUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategoryListView(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategoryDestroyView(generics.RetrieveDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class TovaryCreateView(generics.CreateAPIView):
    serializer_class = TovarySerializer


class TovaryUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = TovarySerializer
    queryset = Tovary.objects.all()


class TovaryListView(generics.ListAPIView):
    serializer_class = TovarySerializer
    queryset = Tovary.objects.all()


class TovaryDestroyView(generics.RetrieveDestroyAPIView):
    serializer_class = TovarySerializer
    queryset = Tovary.objects.all()


class ComentUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = ComentSerializer
    queryset = Coment.objects.all()


class ComentListView(generics.ListAPIView):
    serializer_class = ComentSerializer
    queryset = Coment.objects.all()


class ComentDestroyView(generics.RetrieveDestroyAPIView):
    serializer_class = ComentSerializer
    queryset = Coment.objects.all()


class ComentCreateView(generics.CreateAPIView):
    serializer_class = ComentSerializer

