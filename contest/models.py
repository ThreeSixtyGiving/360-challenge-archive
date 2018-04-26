from django.db import models


QUESTIONS = [
    (1, 'Question One'),
    (2, 'Question Two'),
]


class Submission(models.Model):
    question = models.IntegerField(choices=QUESTIONS)

    title = models.CharField(max_length=256)
    short_description = models.CharField(max_length=256)
    long_description = models.TextField()

    visualization_link = models.URLField()
    source_code_link = models.URLField()
    screenshot_link = models.URLField()


class Applicant(models.Model):
    submission = models.ForeignKey(Submission, related_name='applicants', on_delete=models.PROTECT)

    full_name = models.TextField()
    jobtitle = models.TextField()
    organization = models.TextField(null=True, blank=True)
    picture_link = models.URLField()
    # in the "join" username limit seems to be 39
    github_username = models.CharField(max_length=64, null=True, blank=True)
