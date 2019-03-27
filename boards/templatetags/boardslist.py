from django import template
from ..models import Board
register = template.Library()

@register.simple_tag
def boardlist(count=6):
    return Board.objects.all()