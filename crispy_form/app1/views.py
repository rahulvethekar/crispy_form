from django.shortcuts import render,redirect
from .forms import ProductModelForm
from .models import Product
from django.http import HttpResponse
# Create your views here.
def ProductView(request):
    form = ProductModelForm()
    if request.method == 'POST':
        form = ProductModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('display')
            #return HttpResponse('data inserted!!!!')

    template_name = 'app1/addprod.html'
    context = {'form':form}
    return render(request,template_name,context)

def allProdsDisplay(request):
    data = Product.objects.all()
    context = {'data':data}
    template_name = 'app1/allprod.html'
    return render(request,template_name,context)

def deleteProduct(request,oid):
    obj = Product.objects.get(id=oid)
    obj.delete()
    return redirect('display')

def updateProduct(request,i):
    obj = Product.objects.get(id=i)
    form = ProductModelForm(instance=obj)
    if request.method == 'POST':
        form = ProductModelForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('display')

    template_name = 'app1/addprod.html'
    context = {'form':form}
    return render (request,template_name,context)
