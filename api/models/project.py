from django.db import models
from datetime import timedelta
from django.utils.timezone import now as django_now, localtime

def next_release_7am():
    now = django_now()

    next_seven_am = now.replace(hour=7, minute=0, second=0, microsecond=0)

    if now >= next_seven_am:
        next_seven_am += timedelta(days=1)

    return next_seven_am

class Project(models.Model):
    id = models.SmallAutoField(primary_key=True, unique=True, editable=False, help_text="Id of the project")
    title = models.CharField(max_length=255, help_text="Title of the project")
    description = models.CharField(max_length=255, help_text="Description of the project: typically a short, concise hook")
    starred = models.BooleanField(help_text="True/False for whether the project is starred/pinned")
    created = models.DateTimeField(auto_now_add=True, editable=False, help_text="The creation date-time of the project")
    published = models.DateTimeField(editable=True, db_default=next_release_7am(), help_text="The publish time of the project")
    modified = models.DateTimeField(auto_now=True, help_text="The last modified date-time of the project")
    content = models.TextField(help_text="The html (not react jsx) content of the project. This does not contain images, but links to the images when develiered")
    image = models.ImageField(upload_to="projects/images", help_text="The path to the image in the MEDIA folder of Django")

    def __str__(self):
        return f"{self.title} [{self.created.strftime("%A, %b %d, %Y")}]"