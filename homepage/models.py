from django.db import models
#from litmus.models import Profile

# Model to save notes
class Notes(models.Model):
    diary_notes = models.TextField(blank = False)
    create_time = models.DateTimeField(auto_now_add=True)


