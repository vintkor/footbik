from django import template

register = template.Library()


@register.simple_tag
def is_date_input(field):
    if field.field.widget.__class__.__name__ == 'DateInput':
        return True
    return False
