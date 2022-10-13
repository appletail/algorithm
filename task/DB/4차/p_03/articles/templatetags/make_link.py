from django import template

register = template.Library()
def make_link(content):
    content = content.split()
    for idx in range(len(content)):
        if content[idx].startswith('#'):
            