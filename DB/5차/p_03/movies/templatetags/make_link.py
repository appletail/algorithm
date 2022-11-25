from django import template
from movies.models import Hashtag

register = template.Library()

@register.filter
def hashtag(content):
    content = content.split()

    for idx in range(len(content)):
        if content[idx].startswith('#'):
            hashtag = Hashtag.objects.get(content=content[idx])
            content[idx] = f'<a href="/movies/{hashtag.pk}/hashtag">{hashtag.content}</a>'
    return ' '.join(content)