import decimal
import requests


class CourseHandler:

    def __init__(self):
        self._api_key = '1569DE3D-32B4-4837-AE6D-5F542A29A062'
        self._url = 'https://rest.coinapi.io/v1/'

    def get_course_by_code(self, currency_code):
        method = 'exchangerate/{}/USD'
        headers = {'X-CoinAPI-Key': self._api_key}
        response = requests.get(self._url + method.format(currency_code), headers=headers)

        if response.status_code == 200:
            response_dict = response.json()
            rate = response_dict.get('rate')
            return rate

    def get_all_rates(self, base_currency='USD'):
        method = 'exchangerate/{}'
        headers = {'X-CoinAPI-Key': self._api_key}
        response = requests.get(self._url + method.format(base_currency), headers=headers)

        if response.status_code == 200:
            response_dict = response.json()
            return self._make_dict_from_response(response_dict)

    def _make_dict_from_response(self, response):
        new_dict = {}
        for item in response.get('rates'):
            new_dict[item.get('asset_id_quote')] = item.get('rate')
        return new_dict


class CryptoCurrencyInterface:
    """
    Интерфейс для работы с API EtherScan
    """

    def __init__(self):
        self._token = '234kj3b4h2b3_4b234234nk32j4bk442#3$4n324'
        # self._url = 'https://api.etherscan.io/api'
        self._url = 'http://api-rinkeby.etherscan.io/api'
        # Test api_key
        self.api_key = 'BFKF1G393P95W4R82U3S2Z4STF3E2F6WWY'

    def get_user_balance(self, address):
        """
        Получает баланс пользователя в коинах
        :param address:
        :return: decimal
        """

        print(address)
        balance = decimal.Decimal(5000.54)
        return balance

    def get_all_transactions(self):
        """
        Получает список всех транзакций
        :return: list
        """

        transactions = []
        return transactions

    def add_coins_to_user_balance(self, user_id, amount):
        """
        Добавление коинов пользователю
        :param user_id: string
        :param amount: decimal
        :return: bool
        """

        status = False

        if True:
            status = True

        return status
