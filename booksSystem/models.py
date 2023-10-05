from django.db import models

# Create your models here.


class BooksInStore(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length= 200)

    def __str__(self):
        return self.title
    
class Authors(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    # types_books = models.ForeignKey(TypesOfBooks, on_delete=models.CASCADE)
    # books_store = models.ForeignKey(BooksInStore, on_delete=models.CASCADE)

    # a = TypesOfBooks.objects.create(catgorys="Action and Adventure", names="name")
    # b = BooksInStore.objects.create(title="", decsription="" )
    # c = Author(TypesOfBooks = a, BooksInStore = b)
    # c.save()


class TypesOfBooks(models.Model):
    categorys = [
        ('Action and Adventure', 'Action and Adventure'),
        ('Classic', 'Classic'),
        ('Detective and Mystery', 'Detective and Mystery'),
        ('Pyschology', 'Pyschology'),
        ('Comics', 'Comics'),
        ('Fiction', 'Fiction'),
        ('Crime Fiction', 'Crime Fiction'),
        ('War Story', 'War Story'),
        ('Biography', 'Biography'),

    ]

    types = models.CharField(max_length=100, choices = categorys, default='')
    # authors = models.ForeignKey(Authors, on_delete=models.CASCADE, default='')
    # books = models.ManyToManyField(BooksInStore)
    
    def __str__(self):
        return self.types
    

class ListAllBooks(models.Model):

    types_of_books = models.ForeignKey(TypesOfBooks, on_delete=models.CASCADE, default='', null=True, blank=True)
    authors = models.ForeignKey(Authors, on_delete=models.CASCADE, default='')
    books = models.ManyToManyField(BooksInStore)