from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import TodoForm
from .models import Task

# Create your views here.
def home(request):
	item_list = Task.objects.order_by("-date")
	if request.method == "POST":
		form = TodoForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('todo')

	form = TodoForm()

	page = {
			"forms" : form,
			"list" : item_list,
			"title" : "TODO LIST",

	}
	return render(request, 'index.html', page)
# function to remove tasks

def remove(request, id):
	item=Task.objects.get(id=id)
	item.delete()
	messages.info(request, "Task Removed !!!")
	return redirect ('todo')

def update(request, id):
	item = Task.objects.get(id=id)
	form= TodoForm(instance=item)
	if request.method == "POST":
		form = TodoForm(request.POST,instance=item)
		if form.is_valid():
			form.save()
			return redirect('todo')