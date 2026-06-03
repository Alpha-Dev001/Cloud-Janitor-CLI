import os
from dotenv import load_dotenv

load_dotenv()

ENVIRONMENT = os.environ.get("ENVIRONMENT", "production")
LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO")
DRY_RUN = os.environ.get("DRY_RUN", "true").lower() == "true"