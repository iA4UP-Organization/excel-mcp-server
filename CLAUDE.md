# 🚀 MCP Excel Server Secure — Projet Custom iA4UP

> Fork sécurisé de [haris-musa/excel-mcp-server](https://github.com/haris-musa/excel-mcp-server)
> Sans télémétrie, sans marketplace, sans cloud, 100% privé

> **CLAUDE:** Lis ce fichier EN ENTIER au début de chaque session.

---

## 📍 EMPLACEMENTS CRITIQUES

| Ressource | Emplacement |
|-----------|-------------|
| **Ce fichier (repo GitHub)** | `CLAUDE.md` à la racine du repo |
| **Copie locale (briefing)** | `G:\Mon Drive\iA4UP\Claude\MCP-Custom\Excel\CLAUDE.md` |
| **Repo GitHub** | https://github.com/iA4UP-Organization/excel-mcp-server |
| **Repo source (upstream)** | https://github.com/haris-musa/excel-mcp-server |
| **Ancien repo (inactif)** | https://github.com/iA4UP-Organization/excel-mcp |
| **Organisation GitHub** | `iA4UP-Organization` |

---

## 📋 Origine du Projet

**Source** : [haris-musa/excel-mcp-server](https://github.com/haris-musa/excel-mcp-server) (2 800+ ⭐)
**Fork** : [iA4UP-Organization/excel-mcp-server](https://github.com/iA4UP-Organization/excel-mcp-server)
**Licence** : MIT
**Date du fork** : 08/02/2025
**Auteur original** : Haris Musa

### Pourquoi ce fork (pivot depuis mort-lab)

| Critère | mort-lab (ancien) | haris-musa (actuel) |
|---------|-------------------|---------------------|
| ⭐ Stars | 3 | **2 800+** |
| 🔧 Outils | 20 basiques | **25 complets** |
| 📊 Charts | ❌ | ✅ (line, bar, pie, scatter...) |
| 📈 Pivot Tables | ❌ | ✅ |
| 📋 Tables Excel | ❌ | ✅ |
| 🎨 Conditional Formatting | ❌ | ✅ |
| 🔌 Transports | stdio seul | **stdio + SSE + HTTP** |
| 📦 Publication | Non | **PyPI (`uvx excel-mcp-server`)** |

### Ce qu'on a supprimé ❌

- ~~`manifest.json`~~ → manifest marketplace MCP
- ~~`excel-mcp-server-0.1.7.mcpb`~~ → bundle marketplace
- ~~`.mcpbignore`~~ → config d'exclusion marketplace
- ~~`icon.png`~~ → icône marketplace
- ~~`.github/workflows/publish.yml`~~ → workflow PyPI (compte auteur)
- ~~`TOOLS.md`~~ → doc auteur (documenté ici dans CLAUDE.md)
- ~~`docs/CNAME`~~ → domaine auteur (excelmcpserver.com)
- ~~`docs/index.html`~~ → landing page auteur
- ~~`assets/logo.png`~~ → logo auteur
- ~~`assets/logo.svg`~~ → logo auteur
- ~~`README.md` original~~ → réécrit version iA4UP

### Ce qu'on a ajouté 🛡️

- `config.py` : Configuration ALLOWED_PATHS via variable d'environnement
- `sandbox.py` : Validation anti path-traversal, extension .xlsx, liens symboliques
- `server.py` modifié : Sandbox intégré dans `get_excel_path()` (point central, 25 outils protégés)
- `validation.py` modifié : Formules dangereuses étendues (CALL, REGISTER, EXEC, FILTERXML, REGISTER.ID)
- `README.md` réécrit : Documentation iA4UP avec sécurité documentée
- `CLAUDE.md` : Ce fichier — documentation technique complète

---

## 🏗️ Architecture

```
iA4UP-Organization/excel-mcp-server (GitHub)
├── .gitignore
├── .python-version
├── CLAUDE.md                  # ✅ CE FICHIER (iA4UP)
├── LICENSE                    # MIT
├── README.md                  # ✅ Réécrit iA4UP
├── pyproject.toml             # Config build (hatchling)
├── uv.lock                    # Lock file
└── src/
    └── excel_mcp/
        ├── __init__.py        # Package init
        ├── __main__.py        # CLI Typer (stdio/sse/http)
        ├── server.py          # ✅ Serveur MCP — sandbox intégré dans get_excel_path()
        ├── config.py          # ✅ AJOUTÉ — Configuration ALLOWED_PATHS
        ├── sandbox.py         # ✅ AJOUTÉ — Anti path-traversal, .xlsx only
        ├── validation.py      # ✅ MODIFIÉ — Formules dangereuses étendues
        ├── cell_validation.py # Data validation Excel (dropdown, etc.)
        ├── cell_utils.py      # Utilitaires cellules
        ├── calculations.py    # Application de formules
        ├── chart.py           # Création de graphiques
        ├── data.py            # Lecture/écriture données
        ├── formatting.py      # Mise en forme (conditionnel inclus)
        ├── pivot.py           # Tableaux croisés dynamiques
        ├── sheet.py           # Opérations feuilles (copy, delete, merge...)
        ├── tables.py          # Tables Excel natives
        ├── workbook.py        # Opérations workbook
        └── exceptions.py      # Hiérarchie d'exceptions
```

---

## 🔒 Sécurité (3 couches)

### Couche 1 — Sandboxing des chemins (config.py + sandbox.py)
- **ALLOWED_PATHS** via variable d'environnement (séparés par virgules)
- **Anti path-traversal** : blocage `../` et `~`
- **Extension obligatoire** : `.xlsx` uniquement
- **Liens symboliques** : vérification que la cible reste dans le sandbox
- **Point d'entrée unique** : `get_excel_path()` dans server.py — tous les 25 outils passent par là

### Couche 2 — Formules dangereuses (validation.py)
Fonctions bloquées : `CALL`, `REGISTER`, `REGISTER.ID`, `EXEC`, `INDIRECT`, `HYPERLINK`, `WEBSERVICE`, `DGET`, `RTD`, `FILTERXML`

### Couche 3 — Zéro réseau
- Aucun import réseau dans le code applicatif
- Pas de Smithery, pas de marketplace, pas de télémétrie

---

## 🛠️ Outils Disponibles (25 tools)

| Catégorie | Outils |
|-----------|--------|
| **Workbook** (2) | create_workbook, get_workbook_metadata |
| **Worksheet** (4) | create_worksheet, copy_worksheet, delete_worksheet, rename_worksheet |
| **Data** (2) | read_data_from_excel, write_data_to_excel |
| **Formulas** (2) | apply_formula, validate_formula_syntax |
| **Formatting** (1) | format_range (inclut conditional formatting) |
| **Charts** (1) | create_chart (line, bar, pie, scatter, area, radar, doughnut) |
| **Pivot Tables** (1) | create_pivot_table |
| **Tables** (1) | create_table |
| **Cell Operations** (5) | merge_cells, unmerge_cells, get_merged_cells, copy_range, delete_range |
| **Rows/Cols** (4) | insert_rows, insert_columns, delete_sheet_rows, delete_sheet_columns |
| **Validation** (2) | validate_excel_range, get_data_validation_info |

---

## 🔧 Configuration

### Claude Desktop (Local — stdio)

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

### N8N sur VPS Hostinger (SSE ou HTTP)

```yaml
services:
  excel-mcp:
    build: ./excel-mcp-server
    container_name: excel-mcp-secure
    restart: unless-stopped
    volumes:
      - /data/excel:/data/excel:rw
    environment:
      - ALLOWED_PATHS=/data/excel
      - EXCEL_FILES_PATH=/data/excel
      - FASTMCP_HOST=0.0.0.0
      - FASTMCP_PORT=8017
    ports:
      - "8017:8017"
    networks:
      - n8n-network
```

---

## 📦 Dépendances

```toml
dependencies = [
    "mcp[cli]>=1.10.1",
    "fastmcp>=2.0.0,<3.0.0",
    "openpyxl>=3.1.5",
    "typer>=0.16.0"
]
```

---

## 🎯 Cas d'Usage Prioritaires

1. **Analyse outil cotation BESS** (Savpro) — charts + formules
2. **Base prospection éolien** (Savpro) — pivot tables + filtres
3. **Rapports automatisés** (iA4UP/Savpro via N8N) — formatting conditionnel

---

## 📝 Checklist

### Phase 1 : Nettoyage + Sécurité ✅ TERMINÉE
- [x] Fork haris-musa/excel-mcp-server vers iA4UP-Organization
- [x] Suppression fichiers marketplace (manifest.json, .mcpb, .mcpbignore, icon.png)
- [x] Suppression workflow PyPI publish
- [x] Suppression TOOLS.md auteur
- [x] Ajout config.py (ALLOWED_PATHS)
- [x] Ajout sandbox.py (anti path-traversal, .xlsx, symlinks)
- [x] Modification server.py (sandbox dans get_excel_path, SandboxError)
- [x] Modification validation.py (formules dangereuses étendues)
- [x] Création CLAUDE.md iA4UP

### Phase 1b : Nettoyage cosmétique ✅ TERMINÉE
- [x] Suppression docs/CNAME (domaine auteur excelmcpserver.com)
- [x] Suppression docs/index.html (landing page auteur)
- [x] Suppression assets/logo.png et logo.svg (logos auteur)
- [x] Réécriture README.md (version iA4UP)

### Phase 2 : Tests ⏳ À FAIRE
- [ ] Installer en local avec `pip install -e .` ou `uvx`
- [ ] Tester avec Claude Desktop (mode stdio)
- [ ] Valider les 25 outils
- [ ] Tests sécurité : path traversal, extension, formules bloquées
- [ ] Tester les 3 modes de transport (stdio, SSE, HTTP)

### Phase 3 : Dockerisation & Déploiement ⏳ À FAIRE
- [ ] Dockerfile + docker-compose.yml
- [ ] Tester sur VPS Hostinger + intégrer N8N
- [ ] Tests end-to-end

---

## 📜 Historique

| Date | Action |
|------|--------|
| 04/02/2025 | Fork mort-lab/excel-mcp → Phase 1 sécurité terminée |
| 08/02/2025 | Audit comparatif — décision pivot vers haris-musa |
| 08/02/2025 | Fork haris-musa/excel-mcp-server vers iA4UP-Organization |
| 08/02/2025 | Nettoyage marketplace (manifest, mcpb, icon, workflow PyPI, TOOLS.md) |
| 08/02/2025 | Greffe sécurité : config.py + sandbox.py + server.py + validation.py |
| 08/02/2025 | Création CLAUDE.md — **Phase 1 terminée** |
| 08/02/2025 | Nettoyage cosmétique : docs/, assets/, README.md réécrit — **Phase 1b terminée** |

---

*Projet iA4UP / Raphael Depré — Organisation GitHub : iA4UP-Organization*
