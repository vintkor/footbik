from django import template
from shop.models import Category, Cart, CartItem

register = template.Library()


@register.inclusion_tag('shop/_tag-shop-top-nav.html')
def shop_top_nav_tag():
    categories = Category.objects.filter(level__lte=0)
    return {'categories': categories}


@register.simple_tag
def shop_get_cart_sku(user):
    return CartItem.objects.filter(cart__user=user, cart__is_complete=False).count()
