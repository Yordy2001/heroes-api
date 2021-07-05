from django.shortcuts import get_object_or_404, render
from django.shortcuts import HttpResponse
from .models import Choise, Question
# Create your views here.

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    return render(request, 'polls/detail.htm', {'question':question})

def result(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    
    return  render(request, 'polls/results.html', {'question': question} )

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    try:
        selected_choise = question.choise_set.get(pk=request.POST['choice'])
    except (KeyError, Choise.DoesNotExist):
        #redisplay the question voting form
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choise.",
        })
    else:
        selected_choise.votes +=1
        selected_choise.save()
        '''
            Always return an HttResponseRendirect after successfully dealing
            with POST data. This prevent data from being posted twice if a 
            user hits the back button
        '''

        return HttpResponse("You're voting on question %s." % question_id)

def index(request):

    '''Show the last 5 questions in the home page'''

    lastet_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': lastet_question_list }
    return render (request, 'polls/index.html', context)
