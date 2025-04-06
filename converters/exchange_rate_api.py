import logging
import os
import time
import json
import requests

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ExchangeRateAPI:
    """
    Класс для взаимодействия с API обмена валют.
    """
    BASE_URL = 'https://api.exchangerate-api.com/v4/latest/{}'
    CACHE_FILE = 'exchange_rates.json'
    CACHE_EXPIRATION_TIME = 3600  # Время жизни кеша в секундах (1 час)

    def __init__(self, base_currency='USD'):
        self.base_currency = base_currency
        self.rates = {}

    def _load_from_cache(self):
        """
        Загружает курсы валют из файла кеша, если он еще действителен.
        """
        if os.path.exists(self.CACHE_FILE):
            try:
                with open(self.CACHE_FILE, 'r') as f:
                    data = json.load(f)
                    if time.time() - data['timestamp'] < self.CACHE_EXPIRATION_TIME:
                        return data['rates']
            except (json.JSONDecodeError, KeyError):
                logger.warning("Invalid cache file. Fetching from API.")
        return None

    def _save_to_cache(self, rates):
        """
        Сохраняет актуальные курсы валют в файл кеша.
        """
        try:
            data = {
                'timestamp': time.time(),
                'rates': rates
            }
            with open(self.CACHE_FILE, 'w') as f:
                json.dump(data, f)
        except IOError as e:
            logger.error(f"Error saving to cache: {e}")

    def get_exchange_rate(self, target_currency):
        """
        Получает курс конверсии для указанной валюты.
        :param target_currency: Целевая валюта, в которую необходимо конвертировать
        :return: Обменный курс
        """
        rates = self._load_from_cache()
        if rates:
            return rates[target_currency]

        try:
            url = self.BASE_URL.format(self.base_currency)
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()
            rates = data['rates']
            self._save_to_cache(rates)
            return rates[target_currency]
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching rates from API: {e}")
            return None
        except (json.JSONDecodeError, KeyError) as e:
            logger.error(f"Error processing JSON response: {e}")
            return None