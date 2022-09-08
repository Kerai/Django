from datetime import datetime

from django import template

register = template.Library()


@register.simple_tag()
def ctime(format_string='%d %b %Y'):
    return datetime.utcnow().strftime(format_string)
