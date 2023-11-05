from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.http import HttpResponse
from django.template import loader
from markdown import markdown


from .src.main import generate_readme

def index(request):
    template = loader.get_template("quill_app/index.html")

    return HttpResponse(template.render({}, request))


def submit(request, mode="md"):
    # Get 'repo' from previous form
    repo = request.POST.get("repo")
    branch = request.POST.get("branch")

    if branch == "":
        branch = "main"

    readme_md = generate_readme(repo, "temp.md", branch=branch)
    ContentFile(readme_md)

    if mode == "md":
        # download the readme.md file
        response = HttpResponse(readme_md, content_type='text/plain')
        response['Content-Disposition'] = 'attachment; filename="README.md"'
    elif mode == "html":
        # Convert the markdown to HTML
        readme_html = markdown(readme_md)
        # render the readme.html file
        response = HttpResponse(readme_html, content_type='text/html')
    elif mode == "link":
        # return a link to the readme.md file
        file_name = default_storage.save("out_readme.md", ContentFile(readme_md))
        file_url = default_storage.url(file_name)
        response = HttpResponse(f"<a href='{file_url}'>README.md</a>")
    
    return response
