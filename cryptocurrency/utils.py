import decimal
import requests


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
