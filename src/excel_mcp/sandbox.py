"""
Sandbox de sécurité pour iA4UP Excel MCP Server.

Validation des chemins de fichiers :
- Anti path-traversal (blocage ../)
- Restriction aux ALLOWED_PATHS
- Extension .xlsx obligatoire
- Blocage des liens symboliques sortants
"""

import os
import logging
from pathlib import Path

from .config import get_allowed_paths

logger = logging.getLogger("excel-mcp.sandbox")


class SandboxError(Exception):
    """Erreur de sécurité sandbox."""
    pass


def validate_file_path(filepath: str) -> str:
    """
    Valide et résout un chemin de fichier Excel.
    
    Vérifie :
    1. Pas de séquences path-traversal (../)
    2. Extension .xlsx obligatoire
    3. Chemin résolu dans un ALLOWED_PATHS
    4. Pas de lien symbolique sortant du sandbox
    
    Args:
        filepath: Chemin absolu vers le fichier Excel
        
    Returns:
        Chemin résolu et validé (str)
        
    Raises:
        SandboxError: Si le chemin ne passe pas la validation
    """
    # 1. Bloquer les séquences path-traversal
    if ".." in filepath or "~" in filepath:
        raise SandboxError(
            f"Path-traversal détecté dans le chemin : {filepath}"
        )
    
    # 2. Vérifier l'extension .xlsx
    if not filepath.lower().endswith(".xlsx"):
        raise SandboxError(
            f"Extension non autorisée. Seuls les fichiers .xlsx sont acceptés : {filepath}"
        )
    
    # 3. Résoudre le chemin absolu
    resolved = Path(filepath).resolve()
    
    # 4. Vérifier que le chemin est dans un ALLOWED_PATHS
    allowed_paths = get_allowed_paths()
    
    if not allowed_paths:
        raise SandboxError(
            "Aucun répertoire autorisé configuré. "
            "Définir ALLOWED_PATHS dans les variables d'environnement."
        )
    
    is_allowed = False
    for allowed in allowed_paths:
        try:
            resolved.relative_to(allowed)
            is_allowed = True
            break
        except ValueError:
            continue
    
    if not is_allowed:
        raise SandboxError(
            f"Accès refusé : {filepath} n'est pas dans les répertoires autorisés. "
            f"Répertoires autorisés : {[str(p) for p in allowed_paths]}"
        )
    
    # 5. Vérifier les liens symboliques (ne doivent pas sortir du sandbox)
    if resolved.is_symlink():
        real_target = Path(os.path.realpath(resolved))
        target_allowed = False
        for allowed in allowed_paths:
            try:
                real_target.relative_to(allowed)
                target_allowed = True
                break
            except ValueError:
                continue
        
        if not target_allowed:
            raise SandboxError(
                f"Lien symbolique bloqué : {filepath} pointe vers {real_target} "
                f"(hors des répertoires autorisés)"
            )
    
    logger.debug(f"Chemin validé : {resolved}")
    return str(resolved)
