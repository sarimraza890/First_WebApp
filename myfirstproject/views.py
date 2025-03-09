from django.http import HttpResponse
from django.shortcuts import render
from . import counter

def home (request):
    return render(request,'index.html',{'Key1':'Python code'})

def result (request):
    article= request.GET['article']
    word_count, sorted_dic= counter.count(article)
    return render(request,'result.html',{'art': article, 'count': word_count, 'sorted' : sorted_dic})

def downloads (request):
    return HttpResponse('<h1> No Downloads </h1>')