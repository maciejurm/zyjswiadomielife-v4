from django.shortcuts import render, get_object_or_404, redirect
from .models import Board, Subject, Embed
from comments.forms import SubjectcommentForm, EmbedcommentForm
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView
from django.urls import reverse
from zyjswiadomie.settings import IFRAMELYKEY

import requests
import json

from .forms import SubmitEmbed
from .serializer import EmbedSerializer

@login_required
def save_embed(request):
    if request.method == "POST":
        form = SubmitEmbed(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            board = form.cleaned_data['board']
            r = requests.get('http://iframe.ly/api/oembed?url='+ url + '&api_key=' + IFRAMELYKEY)
            json = r.json()
            if board:
                json['board'] = board.id
            serializer = EmbedSerializer(data=json, context={'request': request})
            if serializer.is_valid():
                embed = serializer.save()
                redir_url = reverse(
                "embededit",
                kwargs={"pk": embed.id})
                return redirect(redir_url)
    else:
        form = SubmitEmbed()

    return render(request, 'embed/embedadd.html', {'form': form})

class EmbedUpdate(UpdateView):
    model = Embed
    fields = ['title', 'description', 'board']
    template_name_suffix = '_update_form'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class BoardsPageView(ListView):
    """
    Basic ListView implementation to call the boards list.
    """
    model = Board
    queryset = Board.objects.all()
    paginate_by = 20
    template_name = 'boards/list.html'
    context_object_name = 'boards'

def boarddetail(request, slug):
    board = get_object_or_404(Board, slug=slug)
    subjects = board.subjects.all()
    embeds = board.embeds.all()

    return render(request, 'board/boarddetail.html',
                {'board': board,
                'subjects': subjects,
                'embeds': embeds})

class UserSubscriptionListView(LoginRequiredMixin, ListView):
    model = Board
    paginate_by = 10
    template_name = 'boards/user_subscription_list.html'
    context_object_name = 'subscriptions'

    def get_queryset(self, **kwargs):
        user = get_object_or_404(User,
                                 username=self.request.user)
        return user.subscribed_boards.all()

@login_required
def feed(request):
    user = get_object_or_404(User, username=request.user)
    boards = user.subscribed_boards.prefetch_related('embeds')
    return render(request, 'boards/feed.html',
                {'boards': boards})

class BoardCreate(LoginRequiredMixin, CreateView):
    model = Board
    fields = ['title', 'image', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

def subjectlist(request):
    subjects = Subject.objects.all()

    return render(request, 'boards/subjectlist.html',
                {'subjects': subjects})

def subjectdetail(request, slug):
    subject = get_object_or_404(Subject, slug=slug)

    comments = subject.subjectcomments.all()
    categories = Board.objects.all()
    random = categories.random(4)

    if request.method == 'POST':
        form = SubjectcommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.author = request.user
            new_comment.subject = subject
            new_comment.save()
    else:
        form = SubjectcommentForm()

    return render(request, 'board/subjectdetail.html',
                {'subject': subject,
                'comments': comments,
                'form': form,
                'random': random})

class SubjectCreate(LoginRequiredMixin, CreateView):

    model = Subject
    fields = ['title', 'body', 'board']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

def embeddetail(request, slug):
    embed = get_object_or_404(Embed, slug=slug)

    comments = embed.embedcomments.all()
    categories = Board.objects.all()
    random = categories.random(4)

    if request.method == 'POST':
        form = EmbedcommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.author = request.user
            new_comment.embed = embed
            new_comment.save()
    else:
        form = EmbedcommentForm()

    return render(request, 'embed/embed_detail.html',
                {'embed': embed,
                'form': form,
                'comments': comments,
                'random': random})

def subscribe(request, board):
    """
    Subscribes a board & returns subscribers count.
    """
    board = get_object_or_404(Board,
                              slug=board)
    user = request.user
    if board in user.subscribed_boards.all():
        board.subscribers.remove(user)
    else:
        board.subscribers.add(user)
    return HttpResponse(board.subscribers.count())

def subscribe_add(request, pk):
    this_board = Board.objects.get(pk=pk)
    this_board.add_user_to_list_of_subscribers(user=request.user)
    return redirect('boardlist')


def subscribe_delete(request, pk):
    this_board = Board.objects.get(pk=pk)
    this_board.remove_user_from_list_of_subscribers(request.user)
    return redirect('boardlist')
