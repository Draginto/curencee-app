import os

class Config:
    SECRET_KEY = os.environ["SECRET_KEY"]
    SQLALCHEMY_DATABASE_URI = os.environ["SQLALCHEMY_DATABASE_URI"] # Replace with postgresql
    CACHE_TYPE = "SimpleCache"  # Replace with Redis
    CACHE_DEFAULT_TIMEOUT = 300
    HCAPTCHA_SITE_KEY = os.environ["HCAPTCHA_SITE_KEY"]
    HCAPTCHA_SITE_SECRET = os.environ["HCAPTCHA_SITE_SECRET"]
    HCAPTCHA_ENABLED = True
