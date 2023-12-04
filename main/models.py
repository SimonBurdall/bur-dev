from django.db import models

class project(models.Model):
    name = models.CharField(max_length=100)
    short_description = models.CharField(max_length=50)
    description = models.TextField()
    grid_image = models.ImageField(upload_to='project_images/',null=True,blank=True)
    hero_image = models.ImageField(null=True,blank=True)
    project_link = models.URLField(null=True,blank=True)
    github_link = models.URLField(null=True,blank=True)
    blog_post = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.name

class project_language(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class project_language_mapping(models.Model):
    language = models.ForeignKey(project_language, on_delete=models.CASCADE)
    project = models.ForeignKey(project, on_delete=models.CASCADE, related_name='language_mappings')

    def __str__(self):
        return f'{self.language} - {self.project.name}'

