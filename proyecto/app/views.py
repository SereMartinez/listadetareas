from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Task;

# Create your views here.
def index(request):
    # template=loader.get_template("app/index.html")
    db_data= Task.objects.all()
    context =  {
        "db_data" : db_data[::-1],
        "update":None

    }

    # return HttpResponse(template.render(context, request))
    return render(request, "app/index.html", context)


def insert(request):
    try:
        task_subject = request.POST["subject"]
        task_descripcion = request.POST["descripcion"]
        if task_descripcion == "" or task_subject == "":
            raise ValueError("El texto no puede estar vacio")
        db_data = Task(subject=task_subject, descripcion=task_descripcion)
        db_data.save()
        return HttpResponseRedirect(reverse("index")) 
    except ValueError as err:
        print (err)
        return HttpResponseRedirect (reverse("index"))

def update(request):
    task_id = request.POST["id"]
    task_subject = request.POST["subject"]
    task_descripcion = request.POST["descripcion"]
    db_data = Task.objects.geet(pk=task_id)
    db_data.save()
    return HttpResponseRedirect(reverse("index"))

def update_form(request, task_id):
    db_data = Task.objects.all()
    db_data_only = Task.objects.get(pk=task_id)
    print(db_data_only)
    context = {
        "db_data": db_data[::-1],
        "update": db_data_only
    }

def delete (request, task_id):
    db_data = Task.objects.filter(id=task_id)
    db_data.delete() 
    return HttpResponseRedirect(reverse("index"))
