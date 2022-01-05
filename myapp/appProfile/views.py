from django.shortcuts import render, HttpResponse

from .models import Project


# Create your views here.


def profile(request):
    """ AGREGAR NUEVAS FILAS A LA TABLA """
    # p1 = Project(title="Curso HTML", description="Descripción del Curso HTML")
    # p1.save()
    # p2 = Project(title="Curso CSS", description="Descripción del Curso CSS")
    # p2.save()
    # p3 = Project(title="Curso DJANGO", description="Descripción del Curso DJANGO")
    # p3.save()

    """ AGREGAR NUEVAS FILAS A LA TABLA """
    projects = Project.objects.all()
    print(projects)

    return HttpResponse(projects)
