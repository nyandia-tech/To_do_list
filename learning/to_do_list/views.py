from django.shortcuts import render,redirect
from .models import Task

# Create your views here.
#create a function to display the tasks
def task_list(request):
    tasks = Task.objects.all()  # Get all the tasks from the database
    if request.method == 'POST':
        #what are we sending to the database
        title = request.POST.get('title') #get the title from the form
        if title:#if we have gotten the title
            #store the task in the database
            Task.objects.create(title=title) #create a new task in the database
            #if the task has not been found   
        return redirect("home") #redirect to the task list page
    return render(request,"todo.html",{"tasks":tasks}) #render the task list page and pass the tasks to the template
    #function to delete a task
def delete_task(request,task_id):
    task = Task.objects.get(id=task_id) #get the task from the database
    task.delete() #delete the task from the database
    return redirect("home") #redirect to the task list page
    #function to mark task as completed
def complete_task(request,task_id):
    task = Task.objects.get(id=task_id) #get the task from the database
    task.completed = True #mark the task as completed
    task.save() #save the changes to the database
    return redirect("home") #redirect to the task list page


