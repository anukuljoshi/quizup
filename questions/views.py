from django.shortcuts import render, get_object_or_404, redirect, reverse

from .models import Question, Answer
from .forms import QuestionCreateForm, AnswerCreateForm

def home_view(request, *args, **kwargs):
    qs = Question.objects.all().order_by('-timestamp')
    context = {
        'object_list' : qs
    }
    return render(request, 'questions/home.html', context=context)


def question_detail_view(request, pk,*args, **kwargs):
    form = AnswerCreateForm()
    ques_qs = get_object_or_404(Question, pk=pk)
    # ques_qs = Question.objects.get(pk=pk)
    ans_qs = Answer.objects.filter(question=pk).order_by('-timestamp')

    if(request.POST):
        form = AnswerCreateForm(request.POST)
        if(form.is_valid()):
            a = form.cleaned_data['answer']
            q = ques_qs
            u = request.user
            answer = Answer(author=u, question=q, answer=a)
            answer.save()
            return redirect(reverse('question-detail', kwargs={'pk':pk}))
    context = {
        'form' : form,
        'ques_object' : ques_qs,
        'ans_object_list' : ans_qs,
    }
    return render(request, 'questions/question-detail.html', context=context)
