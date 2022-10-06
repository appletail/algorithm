import random
from django.shortcuts import render, redirect
from .models import Question, Comment
from .forms import QuestionForm, CommentForm

# Create your views here.
def index(request):
    eithers = Question.objects.all()
    context = {
        'eithers': eithers,
    }
    return render(request, 'eithers/index.html', context)


def create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            detail = form.save()
            return redirect('eithers:detail', detail.pk)
    else:
        form = QuestionForm()
    context = {
        'form': form,
    }
    return render(request, 'eithers/create.html', context)


def detail(request, pk):
    either = Question.objects.get(pk=pk)
    comments = either.comment_set.all()
    comment_form = CommentForm()
    red_count = either.comment_set.filter(pick=0).count()
    blue_count = either.comment_set.filter(pick=1).count()
    if red_count + blue_count == 0:
        red_percent, blue_percent = '0.0', '0.0'
    else:
        red_percent = round(red_count / (red_count + blue_count) * 100, 1)
        blue_percent = round(blue_count / (red_count + blue_count) * 100, 1)
    context = {
        'either': either,
        'comment_form': comment_form,
        'comments': comments,
        'red_count': red_count,
        'blue_count': blue_count,
        'red_percent': red_percent,
        'blue_percent': blue_percent,
    }
    return render(request, 'eithers/detail.html', context)


def update(request, pk):
    either = Question.objects.get(pk=pk)
    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=either)
        if form.is_valid():
            form.save()
            return redirect('eithers:detail', either.pk)
    else:
        form = QuestionForm(instance=either)
    context = {
        'either': either,
        'form': form,
    }
    return render(request, 'eithers/update.html', context)


def delete(request, pk):
    if request.method == 'POST':
        either = Question.objects.get(pk=pk)
        either.delete()
    return redirect('eithers:index')


def comment(request, pk):
    either = Question.objects.get(pk=pk)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment_create = comment_form.save(commit=False)
            comment_create.question = either
            comment_create.save()
            return redirect('eithers:detail', either.pk)


def comment_delete(request, pk, comment_pk):
    either = Question.objects.get(pk=pk)
    if request.method == 'POST':
        comment = Comment.objects.get(pk=comment_pk)
        comment.delete()
    return redirect('eithers:detail', either.pk)


def random_page(request):
    questions = Question.objects.values('pk')
    pk_lst = []
    for value in questions:
        pk_lst.append(value['pk'])
    selected_pk = random.choice(pk_lst)
    return redirect('eithers:detail', selected_pk)
