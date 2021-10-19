from django.db import models
from .team import Team

class Submissions(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, db_index=True)
    stage1_file = models.FileField(upload_to="submissions/stage1")
    stage2_file = models.FileField(upload_to="submissions/stage2")
    stage3_file = models.FileField(upload_to="submissions/stage3")
