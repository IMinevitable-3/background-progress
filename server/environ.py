import os
from dotenv import load_dotenv

load_dotenv()
DJANGO_DEBUG = os.environ.get("DJANGO_DEBUG", True)
SECRET_KEY = os.environ.get(
    "SECRET_KEY", "django-insecure-82t$7=d*8)y!d!x-^qupjm%!9rm1o5z7rc2#6040dfhk!xy+)0"
)
RABBIT_USER = os.environ.get("RABBIT_USER", "user")
RABBIT_PASSWORD = os.environ.get("RABBIT_PASSWORD", "password")
RABBIT_HOST = os.environ.get("RABBIT_HOST", "localhost")
RABBIT_PORT = os.environ.get("RABBIT_PORT", 5672)
REDIS_HOST = os.environ.get("REDIS_HOST", "localhost")
REDIS_PORT = os.environ.get("REDIS_PORT", 6379)
