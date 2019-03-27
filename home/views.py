from django.shortcuts import render
from boards.models import Board, Subject, Embed
from django.views.generic import ListView
from queryset_sequence import QuerySetSequence

class HomeList(ListView):
    queryset = QuerySetSequence(Subject.objects.all(), Embed.objects.all()).order_by('-created_at')
    paginate_by = 20
    context_object_name = 'aktywnosci'
    template_name = 'boards/board_list.html'