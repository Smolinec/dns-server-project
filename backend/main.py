import asyncio
import signal
import sys
from fastapi import FastAPI
import uvicorn
from app.core.dns_resolver import CustomResolver
from app.api.routes import router
import logging

# Konfigurace logování
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("dns-server")

# FastAPI instance
app = FastAPI(
    title="DNS Server API",
    description="REST API pro správu DNS serveru",
    version="1.0.0"
)

# Přidání routeru pro API
app.include_router(router)

# Instance DNS serveru
dns_resolver = CustomResolver()
dns_server = None

# Funkce pro inicializaci DNS serveru
def start_dns_server():
    global dns_server
    try:
        dns_server = DNSServer(dns_resolver, port=53, address="0.0.0.0")
        dns_server.start_thread()
        logger.info("DNS server spuštěn na portu 53")
    except Exception as e:
        logger.error(f"Chyba při spuštění DNS serveru: {e}")
        sys.exit(1)

# Funkce pro zastavení DNS serveru
def stop_dns_server():
    global dns_server
    if dns_server:
        dns_server.stop()
        logger.info("DNS server zastaven")

# Obsluha signálů pro čisté ukončení
def handle_exit(sig, frame):
    logger.info("Zastavuji DNS server...")
    stop_dns_server()
    sys.exit(0)

# Registrujeme obslužné funkce signálů
signal.signal(signal.SIGINT, handle_exit)
signal.signal(signal.SIGTERM, handle_exit)

# Hlavní funkce
if __name__ == "__main__":
    # Spuštění DNS serveru
    start_dns_server()
    
    # Spuštění FastAPI aplikace
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=False)