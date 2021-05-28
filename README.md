# curencee-app
An App that lets you see real-time currency exchange rates and lets you find the nearest exchange place.

## 1. Install requirements.txt 
Install the necessary requirements in order for the app to work.

## 2. Setup your APIs 
- Generate a secret key and add it to your environments or directly replace the `os.environ` with the api in a string.
- Generate a google captcha v2 api key, you'll need the secret and public keys then replace with your environment variable.
- SQLALCHEMY_DATABASE_URI should link directly to your database file/connection to database of choice. The app has been tested with SQLITE AND POSTGRESQL
- Replace the CURRENCY_API environment varialble with an api key from https://openexchangerates.org.
