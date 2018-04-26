from django.contrib import admin

from contest.models import Submission, Applicant


class ApplicantInline(admin.TabularInline):
    model = Applicant
    extra = 0


class SubmissionAdmin(admin.ModelAdmin):
    model = Submission

    inlines = [
        ApplicantInline,
    ]


admin.site.register(Submission, SubmissionAdmin)
