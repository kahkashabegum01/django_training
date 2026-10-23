

from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_POST
from django.http import HttpResponse,HttpResponseRedirect
from database.models import employee
from django.urls  import reverse
# Create your views here.

def newemployeeform(request):
    res=render(request,'newemployeeform.html')
    return res

def saveuser(request):    #cretae recorde c for crud 
    eno=request.POST['eno']
    ename=request.POST['ename']
    esal=request.POST['esal']
    emp=employee(eno=eno,ename=ename,esal=esal)
    emp.save()
    url=reverse('employeelist')
    return HttpResponseRedirect(url)

def employeelist(request):     #read record (r of crud)
    employees=employee.objects.all()   #it return query set 
    res=render(request,'employeelist.html',{'employees': employees})
    return res

def updateemployeeform(request):
    employee_record = get_object_or_404(employee, id=request.GET.get('id'))
    return render(request, 'ateemployeeform.html', {'employee': employee_record})

def updateemployee(request):
    id=request.POST['id']
    eno=request.POST['eno']
    ename=request.POST['ename']
    esal=request.POST['esal']
    employee(id=id,ename=ename,eno=eno,esal=esal).save()
    url=reverse('employeelist')
    return HttpResponseRedirect(url)


@require_POST
def deleteemployee(request):
    emp = get_object_or_404(employee, id=request.POST.get('id'))
    emp.delete()
    url=reverse('employeelist')
    return HttpResponseRedirect(url)





