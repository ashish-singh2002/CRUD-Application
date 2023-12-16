from django.shortcuts import render, redirect
from .models import *

def Insert(request):
    return render(request, "app/insert.html")

def InsertData(request):
    fname = request.POST['fname']
    lname = request.POST['lname']
    email = request.POST['email']
    contact = request.POST['contact']

    newuser = student.objects.create(Firstname=fname, Lastname=lname, Email=email, Contact=contact)
    return redirect("show")

def show(request):
    all_data = student.objects.all()
    return render(request, "app/show.html", {'key1': all_data})

def edit(request, pk):
    get_data = student.objects.get(id=pk)
    return render(request, "app/edit.html", {'key2': get_data})

def update(request, pk):
    udata = student.objects.get(id=pk)
    udata.Firstname = request.POST['fname']
    udata.Lastname = request.POST['lname']
    udata.Email = request.POST['email']
    udata.Contact = request.POST['contact']

    udata.save()
    return redirect("show")

def delete(request,pk):
    ddata = student.objects.get(id=pk)
    ddata.delete()
    return redirect("show")
 