from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Question

# Create your views here.
def index(req):
    lastest_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = ', '.join([q.question_text for q in lastest_question_list])
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': lastest_question_list,
    }
    return HttpResponse(template.render(context, req))
def detail(req, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(req, 'polls/detail.html', {'question': question})
def results(req, question_id):
    response = f"You're looking at the results of question {question_id}"
    return HttpResponse(response)
def vote(req, question_id):
    return HttpResponse(f"You're voting on question {question_id}")