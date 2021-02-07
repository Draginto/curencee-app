# This file will store the currency class alongside the necessary logic needed for conversion.

class Currency:
    def __init__(self, originalPrice, currencyType):
        self.originalPrice = originalPrice
        self.currencyType = currencyType

    def getCurrency(self):
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
        return self.currencyType

    def convertCurrency(self, newCurrencyType: str) -> float:
        api_key = "51b79910546da21412e8c5080e07ba5a"
        endpoint = "convert"
        base = self.getCurrencyType()   # Gets original currency type given in object.
        symbol = newCurrencyType
        amount = self.originalPrice     # The price to convert to new currency.

        complete_url = ("http://data.fixer.io/api/" + endpoint + "?" + "access_key=" + api_key + "&from=" + base +
                        "&to=" + symbol + "&amount=" + str(amount))
        print(complete_url)





