from django.shortcuts import render, get_object_or_404

from .models import Question, Answer

def home_view(request, *args, **kwargs):
    qs = Question.objects.all()
    context = {
        'object_list' : qs
    }
    return render(request, 'questions/home.html', context=context)


def question_detail_view(request, pk,*args, **kwargs):
    ques_qs = get_object_or_404(Question, pk=pk)
    # ques_qs = Question.objects.get(pk=pk)
    ans_qs = Answer.objects.filter(question=pk)
    context = {
        'ques_object' : ques_qs,
        'ans_object_list' : ans_qs,
        'pk' : pk
    }
    return render(request, 'questions/question-detail.html', context=context)