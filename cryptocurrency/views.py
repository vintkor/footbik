from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Currency, SystemSetting


class IcoIndexView(View):

    def get(self, request):
        context = {}
        return render(request, 'cryptocurrency/index.html', context)


class BuyView(View):

    def get(self, request):
        currencies = Currency.objects.filter(is_active=True).values('id', 'code')
        context = {
            'currencies': currencies,
        }
        return render(request, 'cryptocurrency/buy.html', context)

    def post(self, request):
        currency = get_object_or_404(Currency, pk=self.request.POST.get('currency'))
        system_settings = SystemSetting.objects.first()
        course = system_settings.settings.get('coin_course')
        currency_course = round(1 / currency.course, 5)

        context = {
            'currency': currency,
            'address_of_our_wallet': system_settings.settings.get('address_of_our_wallet'),
            'amount_tokens': round(100 / currency_course, 7),
            'course': course,
            'currency_course': currency_course,
        }

        return render(request, 'cryptocurrency/_buy_part.html', context)
