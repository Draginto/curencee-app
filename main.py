from currency import Currency

def main():
    currObject = Currency(34.99, "USD")
    currObject.toCurrency("JPY")

if __name__ == '__main__':
    main()