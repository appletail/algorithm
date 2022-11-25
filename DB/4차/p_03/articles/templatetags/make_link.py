from django import template
from articles.models import Hashtag

register = template.Library()

@register.filter
def make_link(content):
    content = content.split()
    
    for idx in range(len(content)):
        if content[idx].startswith('#'):
            hashtag = Hashtag.objects.get(content=content[idx])
            content[idx] = f'<a href="/articles/{hashtag.pk}/hashtag/">{hashtag.content}</a>'
    return ' '.join(content)
