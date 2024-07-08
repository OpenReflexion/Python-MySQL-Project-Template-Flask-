import logging
from logging.handlers import TimedRotatingFileHandler
import os
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

ENVIRONMENT = os.getenv("ENVIRONMENT")

# Créer un dossier pour les logs si nécessaire
log_directory = "var/logs"
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

# Configuration du format du logging
log_format = "[%(asctime)s][%(levelname)s] : %(pathname)s, %(message)s"
date_format = "%Y-%m-%d %H:%M:%S"

# Ajouter le file handler au logger
logger = logging.getLogger()
logger.setLevel(logging.DEBUG if ENVIRONMENT == "development" else logging.ERROR)

# Handler pour les logs de debug
debug_file_handler = TimedRotatingFileHandler(
    os.path.join(log_directory, f"{ENVIRONMENT.lower()}_debug.log"),
    when="H",
    interval=1,
    backupCount=24
)

debug_file_handler.setFormatter(logging.Formatter(log_format, date_format))
debug_file_handler.setLevel(logging.DEBUG)
logger.addHandler(debug_file_handler)

# Handler pour les logs d'erreur
error_file_handler = TimedRotatingFileHandler(
    os.path.join(log_directory, f"{ENVIRONMENT.lower()}_error.log"),
    when="H",
    interval=1,
    backupCount=24
)
error_file_handler.setFormatter(logging.Formatter(log_format, date_format))
error_file_handler.setLevel(logging.ERROR)
logger.addHandler(error_file_handler)
