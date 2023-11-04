from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template("clauding_app/index.html")

    return HttpResponse(template.render({}, request))


def submit(request):
    # Get 'repo' from previous form
    repo = request.POST.get("repo")

    breakpoint()
    template = loader.get_template("clauding_app/submit.html")


    return HttpResponse(template.render({}, request))