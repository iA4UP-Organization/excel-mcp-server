"""
Configuration sécurisée pour iA4UP Excel MCP Server.

ALLOWED_PATHS : liste de répertoires autorisés (variable d'environnement).
Tout accès fichier en dehors de ces répertoires est bloqué.
"""

import os
from pathlib import Path

def get_allowed_paths() -> list[Path]:
    """
    Récupère les chemins autorisés depuis la variable d'environnement ALLOWED_PATHS.
    
    Format : chemins séparés par des virgules.
    Exemple : ALLOWED_PATHS="G:/Mon Drive/iA4UP,G:/Mon Drive/Savpro"
    
    Si ALLOWED_PATHS n'est pas défini, retourne une liste vide
    (aucun accès fichier autorisé — mode le plus restrictif).
    """
    raw = os.environ.get("ALLOWED_PATHS", "")
    if not raw.strip():
        return []
    
    paths = []
    for p in raw.split(","):
        p = p.strip()
        if p:
            resolved = Path(p).resolve()
            if resolved.is_dir():
                paths.append(resolved)
    
    return paths
