# This file will store the currency class alongside the necessary logic needed for conversion.
import urllib.request, json


class Currency:
    def __init__(self, originalPrice, currencyType):
        self.originalPrice = originalPrice
        self.currencyType = currencyType

    def getCurrencyPrice(self):
        """
        Looks for the original price set in currency specified.
        :return: the value of the currency set.
        """
        return self.originalPrice

    def setCurrency(self, price):
        """
        Replaces the original price set in currency specified.
        :param price: the new price to replace the old price.
        :return: the new listed price of currency.
        """
        self.originalPrice = price
        return self.originalPrice

    def toCurrency(self, toCurrencyType):
        """
        Takes original price given and converts it to the type specified.
        :param toCurrencyType: the new currency to convert to.
        :return: a price in the new currency.
        """
        return self.convertCurrency(toCurrencyType)

    def getCurrencyType(self):
        """
        Method returns the given type by the user.
        :return: Currency type designated by the user as a string.
        """
        return self.currencyType

    def convertCurrency(self, newCurrencyType: str) -> float:
        """
        Get the currency to convert the base currency to target currency.
        :param newCurrencyType: The target currency.
        :return: the total of the converted base currency to target currency.
        """
        endpoint = "latest"
        base = self.getCurrencyType()  # Gets original currency type given in object.
        symbol = newCurrencyType
        amount = self.getCurrencyPrice()  # The price to convert to new currency.

        complete_url = 'https://api.exchangeratesapi.io/' + endpoint + "?base=" + base

        # Pull the exchange rates from the api and decode into object.
        with urllib.request.urlopen(complete_url) as url:
            exchange_rates = json.loads(url.read().decode())

        print("From: $" + str(exchange_rates["rates"][base]) + " TO ¥" + str(exchange_rates["rates"][symbol]))

        total_curr_price = amount * exchange_rates["rates"][symbol]  # Take the amount and multiply by
        print("total: from " + base + " to " + symbol + " " + str(total_curr_price))

        return total_curr_price
