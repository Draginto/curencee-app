class Config:
    SECRET_KEY = '5c753b9873cba5d4f2cb3415a4b1d62f'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db' # Replace with postgresql
    CACHE_TYPE = "SimpleCache"  # Replace with Redis
    CACHE_DEFAULT_TIMEOUT = 300
    HCAPTCHA_SITE_KEY = "f6572226-91bc-4a08-ad81-5f495cd5f9b8"
    HCAPTCHA_SITE_SECRET = "0x730E193eFcDd57EAb7cd74ecB5A4f04d835ec7E2"
    HCAPTCHA_ENABLED = True
