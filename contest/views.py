from urllib.parse import quote_plus

from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect, reverse

from contest.models import Submission, Applicant


def index(request):
    submissions = Submission.objects.all().order_by('-created_at')

    ctx = {
        'submissions': submissions,
    }
    return render(request, 'contest/index.html', ctx)


def terms_and_conditions(request):
    return render(request, 'contest/terms-and-conditions.html')


def faq(request):
    return render(request, 'contest/faq.html')


def cookie_usage(request):
    return render(request, 'contest/cookie-usage.html')


def resources(request):
    return render(request, 'contest/resources.html')


def thanks(request):
    return render(request, 'contest/thanks.html')


def submission(request, id):
    submission = Submission.objects.filter(id=id).prefetch_related('applicants').first()
    if not submission:
        return HttpResponseNotFound()

    tweet_msg = submission.short_description + ' #DiggingTheData bit.ly/2HywPyw'
    tweet_msg = quote_plus(tweet_msg)

    ctx = {
        'submission': submission,
        'tweet_msg': tweet_msg,
    }

    return render(request, 'contest/submission.html', ctx)


def submit(request):
    ctx = {}
    if request.method == "POST":
        submission = Submission(
            question=1,
            title=request.POST.get('project-title'),
            short_description=request.POST.get('short-description'),
            long_description=request.POST.get('long-description'),
            visualization_link=request.POST.get('visualization-link'),
            source_code_link=request.POST.get('sourcecode-link'),
            screenshot_link=request.POST.get('screenshot-link'),
            contact_email=request.POST.get('contact-email'),
        )
        submission.save()

        for key, value in dict(request.POST).items():
            if not (key.startswith('full-name-') and value and value[0]):
                continue

            index = key.replace('full-name-', '')

            Applicant(
                submission=submission,
                full_name=request.POST.get("full-name-{}".format(index)),
                jobtitle=request.POST.get("job-title-{}".format(index)),
                organization=request.POST.get("organization-{}".format(index)),
                picture_link=request.POST.get("profile-image-{}".format(index)),
                github_account=request.POST.get("github-account-{}".format(index)),
            ).save()

        return redirect(reverse('contest_thanks'))

        ctx = {}

    return render(request, 'contest/submit.html', ctx)
