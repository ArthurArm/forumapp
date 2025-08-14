from datetime import datetime

from django import template

register = template.Library()


@register.simple_tag
def current_time(time_format: str = "%d/%m/%Y - %H:%M"):
    return datetime.now().strftime(time_format)
