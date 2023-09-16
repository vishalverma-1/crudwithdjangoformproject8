#---------CREATE OPERATION-----------
from django.shortcuts import render,redirect
from django .http import HttpResponse
from .models import card
from . forms import empform
from django.core.mail import send_mail
def create(request):
    if request.method=='POST':
       form=empform(request.POST)
       if (form.is_valid):
           form.save()
           return redirect('read')
    else:
        form=empform()
        return render(request,'create.html',{'form':form})   
    
#---------------READ OPERATION-------------

def read(request):
    obj=card.objects.all()
    return render(request,'read.html',{'obj':obj})

#---------------DELETE OPERATION-------------

def delete(request,id):
    data=card.objects.get(id=id)
    data.delete()
    return redirect('read')


#---------------EDIT OPERATION---------------



def edit(request,id):
    body=card.objects.get(id=id)
    if request.method=='POST':
      fm=empform(request.POST,instance=body)
      if fm.is_valid:
          fm.save()
          return redirect('read')
      
    else:
        tm=empform(instance=body)
        return render(request,'edit.html',{'tm':tm})
    
def two(request):
    return render(request,'two.html')



