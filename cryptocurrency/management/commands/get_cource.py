from django.core.management.base import BaseCommand, CommandError
from cryptocurrency.utils import CourseHandler
from cryptocurrency.models import Currency


class Command(BaseCommand):
    help = 'Get rates'

    def handle(self, *args, **option):
        print('-' * 120)
        ch = CourseHandler()
        rates = ch.get_all_rates()
        currencies = Currency.objects.filter(is_active=True)

        for currency in currencies:
            rate = rates.get(currency.code)
            if rate:
                currency.course = rate
                currency.save(update_fields=('course',))
