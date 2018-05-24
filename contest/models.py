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

    contact_email = models.EmailField()

    created_at = models.DateTimeField(auto_now_add=True)


class Applicant(models.Model):
    submission = models.ForeignKey(Submission, related_name='applicants', on_delete=models.CASCADE)

    full_name = models.TextField()
    jobtitle = models.TextField()
    organization = models.TextField(null=True, blank=True)
    picture_link = models.URLField()
    github_account = models.URLField()

    created_at = models.DateTimeField(auto_now_add=True)
