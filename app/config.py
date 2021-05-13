import os

class Config:
    SECRET_KEY = os.environ["SECRET_KEY"]
    SQLALCHEMY_DATABASE_URI = os.environ["SQLALCHEMY_DATABASE_URI"] # Replace with postgresql
    CACHE_TYPE = "SimpleCache"  # Replace with Redis
    CACHE_DEFAULT_TIMEOUT = 300
    RECAPTCHA_PUBLIC_KEY = os.environ["RECAPTCHA_SITE_KEY"]
    RECAPTCHA_PRIVATE_KEY = os.environ["RECAPTCHA_SITE_SECRET"]
