from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(req):
    return HttpResponse("Hello, world. You're at polls index")
def detail(req, question_id):
    return HttpResponse(f"You're looking at question {question_id}.")
def results(req, question_id):
    response = f"You're looking at the results of question {question_id}"
    return HttpResponse(response)
def vote(req, question_id):
    return HttpResponse(f"You're voting on question {question_id}")