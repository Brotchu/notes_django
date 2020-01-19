from django.shortcuts import render
from django.http import HttpResponse
import os

# Create your views here.
def home(request):
  return render(request, 'home.html', {'name' : 'Nithin'})

def read(request):
	name = request.GET["note_name"]
	print(name)
	return render(request, 'home.html', {'name' : 'Nithin..'})

def write(request):
	#name = request.GET["note_name"]
	#print(name)
	#content = request.GET["note_conent"]
	return render(request, 'write_note.html')

def save(request):
	name = request.POST["note_header"]
	content = request.POST["note_content"]

	note_file = open("fs/"+name,"w")
	note_file.write(content)
	note_file.close()
	return render(request, 'home.html', {'name' : 'Saved'})
