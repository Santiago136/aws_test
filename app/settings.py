import os

import boto3

SERVICE_NAME = "AWS Test Service"
DEBUG_MODE = True

APP_HOST = os.getenv("APP_HOST", "0.0.0.0")
APP_PORT = int(os.getenv("APP_PORT", 8080))
APP_WORKER_COUNT = int(os.getenv("APP_WORKER_COUNT", 1))

LOG_LEVEL = os.getenv("LOG_LEVEL", "DEBUG")

DATABASE = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")
# DATABASE = boto3.resource('dynamodb', region_name='eu-central-1')

LOG_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "format": "[%(asctime)s] %(levelname)s %(name)s | %(message)s",
            "datefmt": "%d/%b/%Y %H:%M:%S",
        }
    },
    "handlers": {
        "stdout": {
            "level": LOG_LEVEL,
            "class": "logging.StreamHandler",
            "formatter": "default",
        }
    },
    "loggers": {"": {"handlers": ["stdout"], "level": LOG_LEVEL, "propagate": True}},
}
