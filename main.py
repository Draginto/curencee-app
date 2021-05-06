from app.currency import Currency

def main():
    curr_object = Currency(125250, "USD")
    conversion = curr_object.toCurrency("JPY")
    print(conversion)

if __name__ == '__main__':
    main()