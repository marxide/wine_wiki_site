# Django Project Structure

- the structure is as follows: the root dir contains the manage.py script, a nested root project dir containing the project settings, asagi, wsgi, and urls scripts, and finally the apps dirs.
- the apps dir contains the expected admin, apps, models, tests, urls, views, templates, migrations etc.
- asgi.py is for configuring asynchronous web servers, wsgi,py for normal web servers.
- there should be a project level settings.py. (this project currently does not..).
