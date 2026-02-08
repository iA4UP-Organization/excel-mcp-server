# 🛡️ Excel MCP Server Secure — iA4UP

> Fork sécurisé de [haris-musa/excel-mcp-server](https://github.com/haris-musa/excel-mcp-server)
> Manipulation de fichiers Excel (.xlsx) via le protocole MCP — sans cloud, sans télémétrie.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Fork of](https://img.shields.io/badge/fork%20of-haris--musa%2Fexcel--mcp--server-blue)](https://github.com/haris-musa/excel-mcp-server)

---

## Fonctionnalités

- **25 outils** : workbooks, sheets, data, formules, charts, pivot tables, tables Excel, formatting conditionnel
- **3 modes de transport** : stdio, SSE, streamable HTTP
- **Sécurité renforcée (iA4UP)** :
  - Sandboxing des chemins via `ALLOWED_PATHS`
  - Anti path-traversal (`../`, `~`, liens symboliques)
  - Extension `.xlsx` obligatoire
  - Blocage des formules dangereuses (CALL, REGISTER, EXEC, WEBSERVICE, FILTERXML...)
  - Zéro réseau, zéro télémétrie

## Installation

```bash
# Depuis PyPI (base upstream)
uvx excel-mcp-server stdio

# Depuis ce fork (développement local)
git clone https://github.com/iA4UP-Organization/excel-mcp-server.git
cd excel-mcp-server
pip install -e .
excel-mcp-server stdio
```

## Configuration

### Claude Desktop (stdio)

```json
{
  "mcpServers": {
    "excel": {
      "command": "uvx",
      "args": ["excel-mcp-server", "stdio"],
      "env": {
        "ALLOWED_PATHS": "G:/Mon Drive/iA4UP,G:/Mon Drive/Savpro"
      }
    }
  }
}
```

### Variables d'environnement

| Variable | Description | Requis |
|----------|-------------|--------|
| `ALLOWED_PATHS` | Répertoires autorisés (séparés par virgules) | **Oui** |
| `EXCEL_FILES_PATH` | Répertoire par défaut pour SSE/HTTP | SSE/HTTP uniquement |
| `FASTMCP_PORT` | Port du serveur (défaut: 8017) | Non |

## Sécurité

Ce fork ajoute 3 couches de sécurité par rapport à l'upstream :

1. **Sandboxing** — Tout accès fichier est restreint aux `ALLOWED_PATHS`
2. **Formules dangereuses** — 11 fonctions Excel bloquées (CALL, REGISTER, EXEC, etc.)
3. **Zéro réseau** — Aucune dépendance cloud, pas de Smithery, pas de marketplace

Voir [CLAUDE.md](CLAUDE.md) pour la documentation technique complète.

## Crédits

- **Upstream** : [haris-musa/excel-mcp-server](https://github.com/haris-musa/excel-mcp-server) — Merci pour l'excellent travail de base
- **Fork sécurisé** : [iA4UP-Organization](https://github.com/iA4UP-Organization)

## Licence

MIT — voir [LICENSE](LICENSE)
