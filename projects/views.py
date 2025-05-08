from django.shortcuts import render

# will delete this later!
projectList = [
    {
        'id': 1,
        'title': 'Project 1',
        'description': 'Description of Project 1',
        'technologies': ['Python', 'Django'],
        'image': 'project1.jpg',
    },
    {
        'id': 2,
        'title': 'Project 2',
        'description': 'Description of Project 2',
        'technologies': ['JavaScript', 'React'],
        'image': 'project2.jpg',
    },
    {
        'id': 3,
        'title': 'Project 3',
        'description': 'Description of Project 3',
        'technologies': ['HTML', 'CSS'],
        'image': 'project3.jpg',
    }
]

def all_projects(request):
    context = {
        'projects': projectList,
    }
    return render(request, 'projects/all_projects.html', context)


def single_project(request, pk):
    project = None
    for proj in projectList:
        if proj['id'] == pk:
            project = proj
            break
    context = { 'project': project }
    return render(request, 'projects/single_project.html', context)
