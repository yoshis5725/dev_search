from django.shortcuts import render, get_object_or_404, redirect

from projects.forms import ProjectForm
from projects.models import Project


def all_projects(request):
    project_list = Project.objects.all()
    context = {
        'projects': project_list,
    }
    return render(request, 'projects/all_projects.html', context)


def single_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    tags = project.tags.all()
    context = {
        'project': project,
        'tags': tags,
    }
    return render(request, 'projects/single_project.html', context)


# Form for creating a new project
def create_project(request):
    form = ProjectForm()

    # Check if the request method is POST
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            form.save()
            # Redirect to a success page or another view
            return redirect('all_projects')

    context = {'form': form}
    return render(request, 'projects/project_form.html', context)