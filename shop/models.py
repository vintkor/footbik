from django.db import models
from django.utils.translation import ugettext as _
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey
from ckeditor_uploader.fields import RichTextUploadingField
from user_profile.models import User


class Category(MPTTModel):
    """
    Категория товара
    """
    parent = TreeForeignKey(
        'self', verbose_name=_('Родитель'), null=True, blank=True,
        related_name='children', db_index=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, verbose_name=_('Название'))
    slug = models.SlugField(null=True, max_length=230, unique=True)
    created = models.DateTimeField(verbose_name=_('Дата создания'), auto_now_add=True, auto_now=False)

    class Meta:
        verbose_name = _('Категория')
        verbose_name_plural = _('Категории')

    class MPTTMeta:
        order_insertion_by = ['title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('shop:products-in-category', args=[self.slug])

    def has_products(self):
        return self.product_set.all().exists()

    def get_products(self):
        children_categories = [item['id'] for item in self.get_descendants(include_self=True).values('id')]
        return Product.objects.select_related('category').filter(category_id__in=children_categories)


class Product(models.Model):
    """
    Товар
    """
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, verbose_name=_('Название'))
    slug = models.SlugField(null=True, max_length=230, unique=True)
    image = models.ImageField(verbose_name=_('Главное изображение'), blank=True, null=True, upload_to='images/shop/')
    text = RichTextUploadingField(verbose_name=_('Текст'), blank=True, null=True)
    is_virtual = models.BooleanField(default=False, verbose_name=_('Является виртуальным товаром'))
    created = models.DateTimeField(verbose_name=_('Дата создания'), auto_now_add=True, auto_now=False)

    class Meta:
        verbose_name = _('Товар')
        verbose_name_plural = _('Товары')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('shop:product', args=[self.category.slug, self.slug])

    def get_price_range(self):
        """
        Определяет и возвращает min и max цену продукта
        Если вариант продукта только один - возвращает только одну цену
        :return: string
        """
        variants = self.variant_set.all().values_list('price')
        prices = [i[0] for i in variants]
        if len(prices) > 1:
            return '{} - {}'.format(str(min(prices)), str(max(prices)))
        return str(prices[0])

    get_price_range.short_description = _('Цена')

    def get_count_variants(self):
        return self.variant_set.count()

    get_count_variants.short_description = _('Кол-во вариантов')


class Parameter(models.Model):
    """
    Характеристика товара
    """
    title = models.CharField(max_length=200, verbose_name=_('Название'))

    class Meta:
        verbose_name = _('Параметр')
        verbose_name_plural = _('Параметры')

    def __str__(self):
        return self.title


class Value(models.Model):
    """
    Допустимые значения характеристики товара
    """
    parameter = models.ForeignKey(Parameter, on_delete=models.CASCADE, verbose_name=_('Параметр'))
    value = models.CharField(max_length=200, verbose_name=_('Значение'))

    class Meta:
        verbose_name = _('Значение')
        verbose_name_plural = _('Значения')

    def __str__(self):
        return '{} {}'.format(self.parameter, self.value)


class Variant(models.Model):
    """
    Вариант товара (по определённой характеристике)
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_('Товар'))
    value = models.ManyToManyField(Value, verbose_name=_('Набор значений'))
    price = models.DecimalField(verbose_name=_('Цена'), decimal_places=2, max_digits=10)
    quantity = models.PositiveIntegerField(verbose_name=_('Количество'))

    class Meta:
        verbose_name = _('Вариант')
        verbose_name_plural = _('Варианты')

    def __str__(self):
        return '{} - {}'.format(self.product.title, self.price)

    def is_available(self):
        return True if self.quantity > 0 else False

    def make_human_string(self):
        return '; '.join([str(item) for item in self.value.all()])


class ProductParameters(models.Model):
    """
    Характеристики товара (в общем для товара - не для варианта)
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    value = models.ManyToManyField(Value, verbose_name=_('Набор значений'))

    class Meta:
        verbose_name = _('Параметр товара')
        verbose_name_plural = _('Параметры товара')

    def __str__(self):
        return '{}: {}'.format(self.product.title, self.make_human_string())

    def make_human_string(self):
        return '; '.join([str(item) for item in self.value.all()])


class Cart(models.Model):
    """
    Корзина
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('Пользователь'))
    created = models.DateTimeField(verbose_name=_('Дата создания'), auto_now_add=True, auto_now=False)
    is_complete = models.BooleanField(default=False, verbose_name=_('Оформленна'))

    class Meta:
        verbose_name = _('Корзина')
        verbose_name_plural = _('Корзины')

    def __str__(self):
        return str(self.created)

    def get_cart_total_sum(self):
        return sum([item.get_total() for item in self.cartitem_set.all()])

    get_cart_total_sum.short_description = _('Итого')


class CartItem(models.Model):
    """
    Строка корзины - вариан товара
    """
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, verbose_name=_('Корзина'))
    variant = models.ForeignKey(Variant, on_delete=models.CASCADE, verbose_name=_('Вариант'))
    quantity = models.PositiveIntegerField(verbose_name=_('Количество'))
    created = models.DateTimeField(verbose_name=_('Дата создания'), auto_now_add=True, auto_now=False)

    class Meta:
        verbose_name = _('Товар корзины')
        verbose_name_plural = _('Товары корзины')

    def __str__(self):
        return '{} - {}'.format(self.variant, self.quantity)

    def get_total(self):
        return self.variant.price * self.quantity
