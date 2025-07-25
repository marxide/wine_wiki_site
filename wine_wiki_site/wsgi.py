"""
WSGI config for wine_wiki project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from dotenv import load_dotenv
from pathlib import Path

# BASE_DIR = Path(__file__).resolve().parent.parent
# project_folder = os.path.expanduser(
#     BASE_DIR / "wine_wiki_site"
# )  # adjust as appropriate
# load_dotenv(os.path.join(project_folder, ".env"))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wine_wiki_site.dev_settings")

application = get_wsgi_application()
