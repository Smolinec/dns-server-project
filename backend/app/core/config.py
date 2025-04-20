import os

class Config:
    DEBUG = os.getenv("DEBUG", "False") == "True"
    HOST = os.getenv("HOST", "0.0.0.0")
    PORT = int(os.getenv("PORT", 8000))
    DNS_SERVER_PORT = int(os.getenv("DNS_SERVER_PORT", 53))
    DNS_SERVER_ADDRESS = os.getenv("DNS_SERVER_ADDRESS", "0.0.0.0")
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")  # Example for SQLite, change as needed
    ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS", "*").split(",")  # Comma-separated list of allowed origins

config = Config()