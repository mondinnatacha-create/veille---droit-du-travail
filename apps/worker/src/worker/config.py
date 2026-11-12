"""Configuration de l'agent de veille droit du travail (France)."""

AGENT_TITLE = "Veille droit du travail - France"
WORKFLOW_NAME = "veille-droit-travail-fr"
DEFAULT_LIBRARY_ID = "01a1cff3-5e78-745c-aaf0-514d707bd96e"
LLM_MODEL = "mistral-medium-latest"

SOURCES = [
    {
        "name": "Ministere du Travail - Actualites",
        "url": "https://travail-emploi.gouv.fr/rss.xml",
        "kind": "rss",
        "max_items": 15,
    },
    {
        "name": "Vie-publique.fr - Lois",
        "url": "https://www.vie-publique.fr/lois-feeds.xml",
        "kind": "rss",
        "max_items": 12,
    },
    {
        "name": "Vie-publique.fr - Actualites",
        "url": "https://www.vie-publique.fr/actualites-feeds.xml",
        "kind": "rss",
        "max_items": 12,
        "keywords": [
            "travail", "emploi", "salari", "chomage", "retraite", "formation",
            "apprentissage", "syndicat", "convention collective", "entreprise",
            "sante au travail", "discrimination", "salaire", "interim", "cdd", "cdi",
        ],
    },
    {
        "name": "Service-Public.gouv.fr - Actualites professionnels",
        "url": "https://www.service-public.gouv.fr/abonnements/rss/actu-actu-pro.rss",
        "kind": "rss",
        "max_items": 12,
    },
    {
        "name": "Bulletins officiels des ministères sociaux",
        "url": "https://bulletins-officiels.social.gouv.fr/rss.xml",
        "kind": "rss",
        "max_items": 12,
    },
    {
        "name": "URSSAF - Actualites",
        "url": "https://www.urssaf.fr/portail/home/actualites.html",
        "kind": "html",
        "link_pattern": "/accueil/actualites/.+",
        "max_items": 12,
    },
    {
        "name": "Conseil d'Etat - Actualites",
        "url": "https://www.conseil-etat.fr/actualites/",
        "kind": "html",
        "link_pattern": "^/actualites/.+",
        "max_items": 12,
    },
]
