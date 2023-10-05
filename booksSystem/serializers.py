from rest_framework import serializers
from .models import BooksInStore, ListAllBooks, TypesOfBooks, Authors

class Books_InStoreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BooksInStore
        fields = ['title', 'description']

        def create(self, validated_data):
            return BooksInStore.objects.create(**validated_data)

        def update(self, instance, validated_data):
            instance.title = validated_data.get('title', instance.title) 
            instance.description = validated_data.get('description', instance.description)
            instance.save()
            return instance()

class Types_OfBooksSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TypesOfBooks
        fields = ['types']

        def create(self, validated_data):
            return TypesOfBooks.objects.create(**validated_data)

        def update(self, instance, validated_data):
            instance.title = validated_data.get('types', instance.types)
            instance.save()
            return instance()

class Author_sSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Authors
        fields = ['name']

        def create(self, validated_data):
            return Authors.objects.create(**validated_data)

        def update(self, instance, validated_data):
            instance.name = validated_data.get('name', instance.name) 
            instance.save()
            return instance()
        

class ListAllBooks_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ListAllBooks
        fields = ['types_of_books', 'authors', 'books']

        def create(self, validated_data):
            return ListAllBooks.objects.create(**validated_data)

        def update(self, instance, validated_data):
            instance.types_of_books = validated_data.get('types_of_books', instance.types_of_books) 
            instance.authors = validated_data.get('authors', instance.authors) 
            instance.books = validated_data.get('books', instance.books) 
            instance.save()
            return instance()
