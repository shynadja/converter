import logging
from abc import ABC, abstractmethod

from .exchange_rate_api import ExchangeRateAPI


class BaseCurrencyConverter(ABC):
    """
    Базовый класс для конвертера валют.
    """
    def __init__(self, base_currency='USD'):
        self.base_currency = base_currency
        self.exchange_rate_api = ExchangeRateAPI(base_currency)
        self.rate = self.exchange_rate_api.get_exchange_rate(self.target_currency)

    @property
    @abstractmethod
    def target_currency(self):
        """Целевая валюта"""
        pass

    def convert(self, amount):
        """
        Конвертирует сумму из базовой валюты в целевую валюту.
        :param amount: сумма в базовой валюте
        :return: сумма в целевой валюте
        """
        return amount * self.rate


class UsdToRubConverter(BaseCurrencyConverter):
    @property
    def target_currency(self):
        return 'RUB'


class UsdToEurConverter(BaseCurrencyConverter):
    @property
    def target_currency(self):
        return 'EUR'


class UsdToGbpConverter(BaseCurrencyConverter):
    @property
    def target_currency(self):
        return 'GBP'


class UsdToCnyConverter(BaseCurrencyConverter):
    @property
    def target_currency(self):
        return 'CNY'