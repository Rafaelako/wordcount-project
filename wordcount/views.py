import operator

from django.http import HttpResponse
from django.shortcuts import render



def homepage(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def count(request):
    fulltext = request.GET["fulltext"]

    words = fulltext.split()

    dictionary = {}

    for word in words:
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1

    sortedwords = sorted(dictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, "count.html", {"fulltext": fulltext, "count": len(words), "sortedwords": sortedwords})