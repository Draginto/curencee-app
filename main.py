from currency import Currency

def main():
    currObject = Currency(125000, "KRW")
    currObject.toCurrency("USD")

if __name__ == '__main__':
    main()