
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect
from myapp.models import product
from django.urls import reverse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def newproductform(request):
    res=render(request,'newproductlist.html')
    return res


@require_POST
def createproduct(request):
    pid=request.POST['pid']
    pname=request.POST['pname']
    prize=request.POST['prize']
    offer=request.POST['offer']
    pr=product(pid=pid,pname=pname,prize=prize,offer=offer,)
    pr.save()
    url=reverse('read')
    return HttpResponseRedirect(url)

def productlist(request):
    products=product.objects.all()
    res=render(request,'productslist.html',{'products': products})
    return res

def updateproductform(request):
    product_record = get_object_or_404(product, id=request.GET.get('id'))
    return render(request, 'updateproduct.html', {'product': product_record})

@require_POST
def updateproduct(request):
    product_record = get_object_or_404(product, id=request.POST.get('id'))
    product_record.pid=request.POST['pid']
    product_record.pname=request.POST['pname']
    product_record.prize=request.POST['prize']
    product_record.offer=request.POST['offer']
    product_record.save()
    url=reverse('read')
    return HttpResponseRedirect(url)

@require_POST
def deleteproduct(request):
    product_record = get_object_or_404(product, id=request.POST.get('id'))
    product_record.delete()
    return HttpResponseRedirect(reverse('read'))






