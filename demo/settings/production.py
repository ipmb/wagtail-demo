import os

from .base import *

DEBUG = False
SECRET_KEY = os.environ["SECRET_KEY"]

ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "*").split(",")

try:
    from .local import *
except ImportError:
    pass
