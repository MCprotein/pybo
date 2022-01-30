import markdown
from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter()
def sub(value, arg):
    return value - arg


@register.filter()
def mark(value):
    extensions = ["nl2br", "fenced_code"]  # 줄 바꿈, 소스코드 표현을 위한 마크다운의 확장 기능
    return mark_safe(markdown.markdown(value, extensions=extensions))
