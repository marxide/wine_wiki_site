# README

Based on [this tutorial](https://books.agiliq.com/projects/djenofdjango/en/latest/chapter5.html).

## Notes

### Wine List Structure

Rules:

- Categories appear as titles with a horizontal line
- principal varieties (Chardonnay, Pinot Noir etc.) are displayed as follows:
  - subheading country
  - Vintage \t Producer 'Name' \t Subregion Region \t Price
  - each section under the subheading is structured as a 4 column table with varying width
- Red and white varietals are formatted slightly differently:
  - Heading
  - Vintage \t Variety Producer 'Name' \t Subregion Region \t Price
- Champagne is again different:
  - subheadings is village.

As of 2025-05-29

- Wine by the Glass
- White Wine:
  - Champagne:
    - Côte des Bar (Aube)
    - Côte des Blancs
    - Côte de Sézanne
    - Montagne de Reims
    - Vallée de la Marne
  - Sparkling (Australia)
  - Riesling:
    - Australia
    - New Zealand
    - France
    - Austria
    - Germany
  - Semillon and Blends:
    - Australia
  - Pinot Gris:
    - Australia
    - France
  - Sauvignon Blanc and blends:
    - Australia
    - France
  - Pinot Blanc:
    - Australia
  - Chenin Blanc
  - Fiano
  - Viognier
  - White Varietals
  - Chardonnay
- Skin Contact and Amphora
- Rosé Wine
- Chilled Red Wine
- Red Wine:
  - Pinot Noir
  - Nebbiolo
  - Sangiovese
  - Gamay
  - Red Varietals
  - Cabernet Franc
  - Cabernet Sauvignon and blends
  - Merlot
  - Grenache and blends
  - Touriga Nacional and blends
  - Tempranillo
  - Shiraz and blends
- Sweet Wine
- Fortified Wine
  a. Dry Fortified Wine, Sweet Fortified Wine
- Sherry
  - Dry Sherry, Sweet Sherry

## Design

### User Management

See the following: <https://learndjango.com/tutorials/django-login-and-logout-tutorial> for basic setup of user accounts.

### Backup

Database backup is managed with [django-dbbackup](https://pypi.org/project/django-dbbackup/). It is executed with `python manage.py dbbackup` which creates a backup in the dir specified by `DBBACKUP_STORAGE_OPTIONS` in the site settings.py. Restoration from backup is achieved by `python manage.py dbrestore`. See [commands](https://django-dbbackup.readthedocs.io/en/stable/commands.html) for more detail.
