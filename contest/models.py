from django.db import models


QUESTIONS = [
    (1, 'Question One'),
    (2, 'Question Two'),
]


class Submission(models.Model):
    question = models.IntegerField(
        choices=QUESTIONS,
    )

    project_demo_url = models.URLField()
    project_source_url = models.URLField()

    submition_screenshot = models.URLField()

    short_description = models.CharField(max_length=256)
    long_description = models.TextField()


class Applicant(models.Model):
    submission = models.ForeignKey(Submission, related_name='applicants', on_delete=models.PROTECT)

    name = models.TextField()
    organization = models.TextField(null=True, blank=True)
    email = models.EmailField()

    # in the "join" username limit seems to be 39
    github_username = models.CharField(max_length=64, null=True, blank=True)

    picture_url = models.URLField()