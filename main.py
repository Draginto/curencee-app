from app.currency import Currency

def main():
    currObject = Currency(125000, "USD")
    currObject.toCurrency("JPY")

if __name__ == '__main__':
    main()