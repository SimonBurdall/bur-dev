from django.contrib import admin
from .models import project, project_language, project_language_mapping

admin.site.register(project)
admin.site.register(project_language)
admin.site.register(project_language_mapping)
