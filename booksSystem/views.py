from django.shortcuts import render

from rest_framework import viewsets
from .serializers import Books_InStoreSerializer, ListAllBooks_Serializer, Types_OfBooksSerializer, Author_sSerializer
from .models import BooksInStore, TypesOfBooks, Authors, ListAllBooks


from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

class BooksInStoreViewSet(viewsets.ModelViewSet):
    queryset = BooksInStore.objects.all().order_by('title')
    serializer_class = Books_InStoreSerializer

@csrf_exempt
def BooksInStore(request):
    if request.method == "GET":
        books = BooksInStore.objects.all()
        serializer = Books_InStoreSerializer(BooksInStore, many=True)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = Books_InStoreSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)     

class TypesOfBooksViewSet(viewsets.ModelViewSet):
    queryset = TypesOfBooks.objects.all().order_by('types')
    serializer_class = Types_OfBooksSerializer

@csrf_exempt
def TypesOfBooks (request):
    if request.method == "GET":
        typess = TypesOfBooks.objects.all()
        serializer = Types_OfBooksSerializer(TypesOfBooks, many=True)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = Types_OfBooksSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)     

class AuthorsViewSet(viewsets.ModelViewSet):
    queryset = Authors.objects.all().order_by('name')
    serializer_class = Author_sSerializer

@csrf_exempt
def Authors(request):
    if request.method == "GET":
        authorss = Authors.objects.all()
        serializer = Author_sSerializer(Authors, many=True)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = Author_sSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)     
    


class LiListAllBooksViewSet(viewsets.ModelViewSet):
    queryset = ListAllBooks.objects.all().order_by('authors')
    serializer_class = ListAllBooks_Serializer

@csrf_exempt
def ListAllBooks(request):
    if request.method == "GET":
        list_of_books = ListAllBooks.objects.all()
        serializer = ListAllBooks_Serializer(ListAllBooks, many=True)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ListAllBooks_Serializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)     

############# Request and Response ######


@api_view(['GET', 'POST'])
def BooksInStore(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = BooksInStore.objects.all()
        serializer = Books_InStoreSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = Books_InStoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
