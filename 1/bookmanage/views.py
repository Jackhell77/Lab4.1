from django.shortcuts import render
from django.http import HttpResponse
import django
from django.template import Context
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from bookmanage.models import Book,Author
def book(request):
    c = Context({"book_list": Book.objects.all(),"head":"All books"})
    return render_to_response("all_book.html", c)
def insertBook(request):
    if request.POST:
        post = request.POST
        __Author = Author.objects.filter(Name = post["AuthorName"])
        if __Author:
            for author in __Author:
                new_book = Book(
                ISBN = post["ISBN"],
                Title = post["Title"],
                AuthorID = author,
                Publisher = post["Publisher"],
                PublishDate = post["PublishDate"],
                Price = post["Price"])            
                new_book.save()            
            return render_to_response("insertBook.html")
        else:
            return render_to_response("insertAuthor.html",{
                "ISBN":post["ISBN"],
                "Title":post["Title"],
                "AuthorName":post["AuthorName"],
                "Publisher":post["Publisher"],
                "PublishDate":post["PublishDate"],
                "Price":post["Price"],
            })
    return render_to_response("insertBook.html")
def insertAuthor(request):
    if request.POST:
        post = request.POST
        new_author = Author(
            AuthorID = post["AuthorID"],
            Name =  post.get('_AuthorName',False),
            Age = post["Age"],
            Country = post["Country"]
        )
        new_author.save()
        new_book = Book(
            ISBN = post.get('ISBN',False),
            Title = post.get('Title',False),
            AuthorID = new_author,
            Publisher = post.get('Publisher',False),
            PublishDate = post.get('PublishDate',False),
            Price = post.get('Price',False)
        )
        new_book.save()
        return HttpResponseRedirect("/book/")
    return render_to_response("insertAuthor.html")
def delete(request):
    ISBN = request.GET["ISBN"] 
    book = Book.objects.get(ISBN=int(ISBN))
    book.delete()
    return HttpResponseRedirect("/all_book/")
def update(request):
    ISBN = request.GET["ISBN"] 
    book = Book.objects.get(ISBN=int(ISBN)) 
    #__Author = Author.objects.filter(Name = request.POST["AuthorName"])
    if request.POST:
        __Author = Author.objects.filter(AuthorID = request.POST["AuthorID"])
        if __Author:   
            for author in __Author:      
                post = request.POST 
                book.AuthorID = author
                book.Publisher = post["Publisher"]
                book.PublishDate = post["PublishDate"]
                book.Price = post["Price"]
                book.save()
                return HttpResponseRedirect("/all_book/")
        else:
            return render_to_response("insertAuthor.html",
                {"ISBN":book.ISBN,
                "Title":book.Title,
                "AuthorName":request.POST["AuthorName"],
                "AuthorID":request.POST["AuthorID"],
                "Publisher":book.Publisher,
                "PublishDate":book.PublishDate.strftime('%Y-%m-%d'),
                "Price":book.Price
                })
        
    return render_to_response("update.html",{"book":book,"PublishDate":book.PublishDate.strftime('%Y-%m-%d')})
def  search(request):
    if request.POST:
        __Author = Author.objects.filter(Name = request.POST["AuthorName"])
        if __Author:
            for author in __Author:
                book = Book.objects.filter(AuthorID = author)
            return render_to_response("all_book.html",{"book_list":book,"head":"Search result"}) 
        return render_to_response("all_book.html",{"book_list":[],"head":"Search result"})
    return render_to_response("search.html")
    
# Create your views here.
