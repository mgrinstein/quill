from django.http import HttpResponse
from django.template import loader
from markdown import markdown


from .src.main import generate_readme

def index(request):
    template = loader.get_template("clauding_app/index.html")

    return HttpResponse(template.render({}, request))


def submit(request):
    # Get 'repo' from previous form
    repo = request.POST.get("repo")
    branch = request.POST.get("branch")

    if branch == "":
        branch = "main"

    readme_md = generate_readme(repo, branch)

    # Convert the markdown to HTML
    readme_html = markdown(readme_md)

    # return the readme.md file
    # response = HttpResponse(readme_md, content_type='text/plain')
    # response['Content-Disposition'] = 'attachment; filename="README.md"'

    # render the readme.html file
    response = HttpResponse(readme_html, content_type='text/html')
    
    return response
