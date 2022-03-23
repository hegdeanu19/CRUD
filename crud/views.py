from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import StudentForm
from .models import student

# Create your views here.
def add(request):
    form=StudentForm(request.POST or None)
    #Student=student.objects.all()

    if form.is_valid():
        form.save()
    return render(request,'add.html',{'form':form})

def show(request):
    Student=student.objects.all()
    return render(request,'show.html',{'Student':Student})

def update(request,id):
    Student=student.objects.get(id=id)
    form=StudentForm(request.POST,instance=Student)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')
    return render(request,'update.html',{'Student':Student}) 

def delete  (request,id):
    form=student.objects.get(id=id)
    form.delete()
    return HttpResponseRedirect('/')
           
