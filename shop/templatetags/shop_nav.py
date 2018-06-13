from django import template
from shop.models import Category


register = template.Library()


@register.inclusion_tag('shop/_tag-shop-top-nav.html')
def shop_top_nav_tag():
    categories = Category.objects.filter(level__lte=0)
    return {'categories': categories}
