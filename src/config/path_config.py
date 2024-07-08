import os
from dotenv import load_dotenv

load_dotenv()

class PathConfig:
    # Chemin absolu vers le répertoire de base du projet
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    
    # Chemin absolu vers le répertoire docs
    DOCS_DIR = os.path.join(BASE_DIR, 'docs')
