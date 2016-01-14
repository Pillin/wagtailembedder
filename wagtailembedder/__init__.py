from django.db.models import options as django_options


django_options.DEFAULT_NAMES = django_options.DEFAULT_NAMES + ('embedder_snippet',)
